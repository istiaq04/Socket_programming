import socket
import os

HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 4096


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("[+] Connected to FTP Server!")
    print("Commands: LIST | DOWNLOAD <file> | UPLOAD <file> | EXIT\n")

    while True:
        user_input = input("ftp> ").strip()
        if not user_input:
            continue

        parts = user_input.split()
        cmd = parts[0].upper()

        if cmd == "LIST":
            client.sendall("LIST".encode('utf-8'))
            response = client.recv(BUFFER_SIZE).decode('utf-8')
            print("\n--- Directory List ---")
            print(response)
            print("-----------------------\n")

        elif cmd == "DOWNLOAD":
            if len(parts) < 2:
                print("Usage: DOWNLOAD <filename>")
                continue
            filename = parts[1]
            client.sendall(f"DOWNLOAD {filename}".encode('utf-8'))
            response = client.recv(1024).decode('utf-8')

            if response.startswith("OK"):
                filesize = int(response.split()[1])
                client.sendall("READY".encode('utf-8'))

                received_bytes = 0
                with open("downloaded_" + filename, 'wb') as f:
                    while received_bytes < filesize:
                        chunk = client.recv(min(BUFFER_SIZE, filesize - received_bytes))
                        if not chunk:
                            break
                        f.write(chunk)
                        received_bytes += len(chunk)
                print(f"[+] File '{filename}' downloaded successfully!\n")
            else:
                print(f"[-] {response}\n")

        elif cmd == "UPLOAD":
            if len(parts) < 2:
                print("Usage: UPLOAD <filename>")
                continue
            filename = parts[1]
            if not os.path.exists(filename):
                print("[-] Local file not found.\n")
                continue

            filesize = os.path.getsize(filename)
            client.sendall(f"UPLOAD {filename} {filesize}".encode('utf-8'))

            if client.recv(1024).decode('utf-8') == "READY":
                with open(filename, 'rb') as f:
                    while chunk := f.read(BUFFER_SIZE):
                        client.sendall(chunk)
                print(f"[+] {client.recv(1024).decode('utf-8')}\n")

        elif cmd == "EXIT":
            client.sendall("EXIT".encode('utf-8'))
            print("Disconnected.")
            break

        else:
            print("[-] Invalid Command.\n")

    client.close()


if __name__ == "__main__":
    start_client()