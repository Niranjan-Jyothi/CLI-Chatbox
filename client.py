import socket

HEADER = 16
PORT = 6666
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
TO_DISCONNECT = '!DISCONNECT!'

client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client_socket.connect(ADDR)

def send(msg):
    msg = msg.encode(FORMAT)
    msg_l = len(msg)
    msg_l = str(msg_l).encode(FORMAT)
    msg_l += b' ' * (HEADER - len(msg_l))
    client_socket.send(msg_l)
    client_socket.send(msg)

def user_input():
    connection = True
    while connection:
      a = input("Enter your text : ")
      send(a)
      if a==TO_DISCONNECT:
          connection = False
          print(client_socket.recv(64).decode(FORMAT))

user_input()