import socket
import os
import threading

HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 4096


def handle_client(conn, addr):
    print(f"[+] Connected by {addr}")
    while True:
        try:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break

            parts = data.strip().split()
            cmd = parts[0].upper() if parts else ""

            # 1. Directory Content View
            if cmd == "LIST":
                files = os.listdir('.')
                file_list = "\n".join(files) if files else "Directory is empty."
                conn.sendall(file_list.encode('utf-8'))

            # 2. File Download
            elif cmd == "DOWNLOAD":
                if len(parts) < 2:
                    conn.sendall("ERROR Usage: DOWNLOAD <filename>".encode('utf-8'))
                    continue
                filename = parts[1]
                if os.path.exists(filename) and os.path.isfile(filename):
                    filesize = os.path.getsize(filename)
                    conn.sendall(f"OK {filesize}".encode('utf-8'))

                    if conn.recv(1024).decode('utf-8') == "READY":
                        with open(filename, 'rb') as f:
                            while chunk := f.read(BUFFER_SIZE):
                                conn.sendall(chunk)
                else:
                    conn.sendall("ERROR File not found".encode('utf-8'))

            # 3. File Upload
            elif cmd == "UPLOAD":
                if len(parts) < 3:
                    conn.sendall("ERROR Usage: UPLOAD <filename> <filesize>".encode('utf-8'))
                    continue
                filename = parts[1]
                filesize = int(parts[2])
                conn.sendall("READY".encode('utf-8'))

                received_bytes = 0
                with open("uploaded_" + filename, 'wb') as f:
                    while received_bytes < filesize:
                        chunk = conn.recv(min(BUFFER_SIZE, filesize - received_bytes))
                        if not chunk:
                            break
                        f.write(chunk)
                        received_bytes += len(chunk)

                conn.sendall("SUCCESS Upload complete".encode('utf-8'))

            elif cmd == "EXIT":
                break

            else:
                conn.sendall("ERROR Unknown command".encode('utf-8'))

        except Exception as e:
            print(f"[-] Error: {e}")
            break

    conn.close()
    print(f"[-] Disconnected {addr}")


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[*] FTP Server running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start_server()