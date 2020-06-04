import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

ALLOW = 2048
PORT = 6666
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
TO_DISCONNECT = '!DISCONNECT!'

client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client_socket.connect(ADDR)

publicKey = client_socket.recv(1024)
publicKey = RSA.importKey(publicKey)
cipher_rsa = PKCS1_OAEP.new(publicKey)

def send(msg):
    cipher_rsa = PKCS1_OAEP.new(publicKey)
    client_socket.send(cipher_rsa.encrypt(msg.encode('utf-8')))
    command_ack = client_socket.recv(1024).decode(FORMAT)
    print(command_ack)
    return False

def user_input():
    valid_username = False
    while not valid_username:
        USERNAME = input("Enter your Username(unique) : ")
        client_socket.send(cipher_rsa.encrypt(USERNAME.encode('utf-8')))
        valid_username = eval(client_socket.recv(16).decode(FORMAT))
    connection = True
    while connection:
      a = input("Enter your text/command($) : ")
      if a!="":
        send(a)
        if a==TO_DISCONNECT:
            connection = False
            print(client_socket.recv(64).decode(FORMAT))

user_input()


