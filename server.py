import socket
import threading
import file_handler

BUFFSIZE = 1024
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


# Starting server and accepting clients.
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        # creating a thread for each client that connects.
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


# Recevies function from "file_handler" file
def handle_files(data):
    if not data:
        resp = "empty"

    elif data[0] == "ls":
        resp = FILES.ls()
        resp = " ".join(resp)

    elif data[0] == "size":
        resp = FILES.size(data[1])
        resp = "Filesize in bytes: " + str(resp)

    elif data[0] == "rm":
        resp = FILES.rm(data[1])
        resp = str(resp)

    elif data[0] == "quit":
        resp = "quit"

    return resp


# Sending and receiving data from clients.
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # Using split() so the recieved data is indexed and we can call on the first word in recv data as function.
        data = conn.recv(BUFFSIZE).decode(FORMAT).split()
        resp = handle_files(data)
        if resp == "quit":
            connected = False
            resp = "Disconnected from server"

        print(f"[{addr}] {data}")

        conn.send(resp.encode(FORMAT))
    print(f"{addr} 'DISCONNECTED'")

    conn.close()


path = "/Users/fransgabro/slutuppgift2/devops20_python_slutuppgift/slutuppgift"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print("[STARTING] server is starting...")
FILES = file_handler.File_handler(path)
start()
