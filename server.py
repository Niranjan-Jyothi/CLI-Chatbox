import socket
import threading

HEADER = 16
PORT = 6666
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
TO_DISCONNECT = '!DISCONNECT!'

server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_socket.bind(ADDR)

def each_client(data , addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connection = True
    while connection:
        msg_l = data.recv(HEADER).decode(FORMAT)
        if msg_l:
          msg_l = int(msg_l)
          msg = data.recv(msg_l).decode(FORMAT)
          if (msg == TO_DISCONNECT):
              connection = False
              print(f"{addr} has been disconnected")
              data.send("You Have Been Disconnected From The Server".encode(FORMAT))

          print(f'{addr} {msg}')
    data.close()


def start_server():
    server_socket.listen()
    while True:
        data , addr = server_socket.accept()
        thread = threading.Thread(target= each_client , args=(data , addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}" )

print(f"[SERVER STARTING] Server starting on {SERVER} \n")
start_server()