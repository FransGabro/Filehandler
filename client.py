import socket

BUFFSIZE = 1024
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print("'Note' Type a command and a space infront of the file you choose")
print(" ")
print("Commands:")
print("ls = List all files in directory\nsize = print the size of a file\nrm = Remove a file")


# sending and recevieng messages from server
def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    msg_rcv = client.recv(BUFFSIZE).decode(FORMAT)
    return msg_rcv


msg = ""
while msg != "quit":
    msg = input()
    resp = send(msg)
    print(resp)
