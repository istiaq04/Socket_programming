# Multi-User TCP Chat Application

## Project Overview

This project is a multi-user chat application built in Python using low-level network sockets and multithreading. It demonstrates the core principles of client-server architecture over TCP/IP, allowing multiple users to connect to a central server simultaneously and exchange text messages in real time.

The application consists of two components:

- **Server:** Manages client connections and message routing.
- **Client:** Allows an individual user to join the chat, send messages, and receive messages from other connected users.

This project was developed to demonstrate a practical understanding of socket programming, concurrent connection handling, and real-time communication design.

---

## Features

- Real-time, multi-user text chat over a TCP connection
- Concurrent handling of multiple clients using threading
- Broadcast messaging: messages sent by a client are delivered to other connected clients
- Join and leave notifications shown to users
- Simple username-based identification for each session
- Graceful client disconnect using the `/quit` command
- Server-side logging of connections, disconnections, and messages
- Works on a local machine using localhost
- Supports communication over a Local Area Network (LAN)

---

## Technologies Used

- **Python 3** - Core programming language
- **socket module** - Used to create TCP client-server connections
- **threading module** - Used to handle multiple client connections concurrently
- **Standard Input/Output (CLI)** - Used for user interaction

No third-party libraries or external dependencies are required.

---

## System Architecture

The application follows a centralized client-server architecture.

```text
                       +----------------+
                       |     Server     |
                       |   server.py    |
                       +----------------+
                         /      |      \
                        /       |       \
                       /        |        \
                      /         |         \
             +-------------+ +-------------+ +-------------+
             |   Client 1  | |   Client 2  | |   Client 3  |
             |   client.py | |   client.py | |   client.py |
             +-------------+ +-------------+ +-------------+
```

### Communication Flow

1. The server binds to a host and port.
2. The server listens for incoming connections.
3. Each client establishes a TCP connection with the server.
4. The client provides a username.
5. The server creates a dedicated thread for each connected client.
6. When a client sends a message, the server receives it.
7. The server broadcasts the message to the other connected clients.
8. Each client uses a listener thread to receive incoming messages.
9. When a client disconnects, the server removes it from the active client list.
10. The server notifies the remaining users about the disconnection.

---

## Requirements

Before running the project, make sure the following are available:

- Python **3.7 or higher**
- A terminal or command prompt
- Network access between server and client machines
- No additional Python packages are required

---

## Getting Started

### 1. Download or Clone the Project

Clone the repository using:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Then enter the project directory:

```bash
cd Socket_programming
```

The project should contain:

```text
Socket_programming/
│
├── server.py
├── client.py
└── README.md
```

---

### 2. Start the Server

Open a terminal in the project folder and run:

```bash
python server.py
```

By default, the server listens on:

```text
Host: 0.0.0.0
Port: 5555
```

A custom host and port can optionally be specified:

```bash
python server.py <host> <port>
```

Example:

```bash
python server.py 0.0.0.0 5555
```

The server will continue running and wait for clients to connect.

---

### 3. Start One or More Clients

Open another terminal and run:

```bash
python client.py 127.0.0.1 5555
```

For multiple users, open multiple terminal windows and run the client in each terminal.

If connecting from another computer on the same LAN, replace `127.0.0.1` with the IP address of the computer running the server.

Example:

```bash
python client.py 192.168.1.10 5555
```

---

### 4. Join the Chat

When the client starts, it will ask for a username.

Enter a username and start chatting.

Example:

```text
Enter your username: Alice
```

After connecting, type any message and press **Enter** to send it to the other connected users.

Example:

```text
Alice: Hello everyone!
```

Other connected clients will receive the message in real time.

---

## Login Credentials

This application does not use a fixed username/password authentication system.

Instead, each client chooses a display username when connecting to the server.

There are:

- No predefined usernames
- No passwords
- No fixed login credentials
- No authentication system

Any username entered at connection time can be used to identify the client for that session.

---

## Available Commands

| Command | Description |
|---|---|
| `<any text>` | Sends the typed message to connected clients |
| `/quit` | Disconnects the client gracefully |

The server does not require interactive commands after startup.

The server continues running until it is manually stopped using:

```text
Ctrl + C
```

---

## Testing

The application was tested using the following scenarios.

### Single Client Connection

Verified that a client can connect to the server, provide a username, and receive a welcome message.

### Multiple Client Connections

Verified that multiple clients can connect to the server simultaneously and exchange messages in real time.

### Join/Leave Notifications

Verified that users receive notifications when another user joins or leaves the chat.

### Disconnect Handling

Verified that using `/quit` or abruptly closing a client removes the client from the server's active list without crashing the server.

### Concurrent Messaging

Verified that multiple clients can send messages at the same time without blocking one another due to threaded handling on both the server and client sides.

Testing was performed locally using multiple terminal instances on the same machine through:

```text
127.0.0.1
```

---

## Learning Objectives

Through this project, the following concepts were studied and applied:

- Fundamentals of network sockets
- TCP/IP communication
- Client-server architecture
- `bind()`
- `listen()`
- `accept()`
- `connect()`
- Concurrent programming using threads
- Handling multiple simultaneous connections
- Managing shared client data across multiple threads
- Application-level message communication
- Network error handling
- Handling unexpected client disconnections gracefully

---

## Limitations

The current implementation has the following limitations:

- No message encryption
- Messages are transmitted as plain text
- No persistent chat history
- No authentication system
- Usernames are not password-protected
- Duplicate usernames are possible
- No private/direct messaging
- All messages are broadcast to connected users
- Not hardened for public Internet deployment
- No graphical user interface
- Interaction is limited to the command line

---

## Future Improvements

Possible future improvements include:

- Add SSL/TLS encryption to secure transmitted data
- Implement username and password authentication
- Enforce unique usernames
- Add private one-to-one messaging
- Store chat history in a database
- Create a graphical user interface using Tkinter
- Add file sharing between connected clients
- Implement chat rooms or channels
- Add online/offline status indicators
- Add message delivery/read receipts
- Improve security for Internet-based deployment

---

## Project Structure

```text
Socket_programming/
│
├── server.py
├── client.py
└── README.md
```

### `server.py`

The server-side program that:

- Creates the server socket
- Accepts incoming client connections
- Creates threads for connected clients
- Receives messages
- Broadcasts messages
- Handles client disconnections

### `client.py`

The client-side program that:

- Connects to the server
- Allows the user to enter a username
- Sends messages to the server
- Receives messages from other users
- Uses a listener thread for incoming messages
- Supports the `/quit` command

### `README.md`

This file contains the project description, features, requirements, installation and execution instructions, testing information, limitations, and future improvements.

---

## Author

**Istiaq Ahmed Srabon**

Computer Science and Engineering  
Southeast University

---

## Conclusion

This project demonstrates the fundamental concepts of socket programming and client-server communication using Python. It provides practical experience with TCP connections, multithreading, message broadcasting, concurrent client handling, and network communication.

The project shows how a centralized server can manage multiple clients simultaneously and provide real-time communication between connected users.

---

## License

This project was developed for educational purposes as part of a Socket Programming homework assignment.
