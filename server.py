import socket
import threading
from Cryptodome.PublicKey import RSA
from Cryptodome import Random
from Cryptodome.Cipher import PKCS1_OAEP
import subprocess

ALLOW = 2048
PORT = 6666
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
TO_DISCONNECT = '!DISCONNECT!'


server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_socket.bind(ADDR)

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
publickey = key.publickey()
decipher_rsa = PKCS1_OAEP.new(key)


def each_client(data , addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connection = True
    data.send(publickey.exportKey())
    while connection:
        msg = decipher_rsa.decrypt(data.recv(ALLOW)).decode(FORMAT)
        if msg:
          if (msg == TO_DISCONNECT):
              connection = False
              print(f"{addr} has been disconnected")
              data.send("You Have Been Disconnected From The Server".encode(FORMAT))
          elif msg[0]=='$':
              msg= msg[1:len(msg)]
              try :
                a = subprocess.run(msg.split())
                if a.returncode==0:
                    data.send("Command Success".encode(FORMAT))
                else: data.send("Command Error".encode(FORMAT))
              except FileNotFoundError:
                  data.send("Command Error".encode(FORMAT))
          else:

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