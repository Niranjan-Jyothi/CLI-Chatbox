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

def send(msg,is_cmd):
    cipher_rsa = PKCS1_OAEP.new(publicKey)
    client_socket.send(cipher_rsa.encrypt(msg.encode('utf-8')))
    if is_cmd :
        command_return = client_socket.recv(1024).decode(FORMAT)
        print(command_return)
    return False


def user_input():
    user_name = input(Enter your Username : )
    connection = True
    is_cmd = False
    while connection:
      a = input("Enter your text : ")
      if a:
        if a[0]=='$':
          is_cmd = True
        is_cmd = send(a,is_cmd)
        if a==TO_DISCONNECT:
            connection = False
            print(client_socket.recv(64).decode(FORMAT))

user_input()

