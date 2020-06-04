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
USERS = {}

server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_socket.bind(ADDR)

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
publickey = key.publickey()
decipher_rsa = PKCS1_OAEP.new(key)

def each_client(data , addr):
  try:
    valid_client = False
    while not valid_client:
     username =  decipher_rsa.decrypt(data.recv(ALLOW)).decode(FORMAT)
     if username!="":
       if username in USERS.keys():
           data.send("False".encode(FORMAT))
       else :
           USERS.update({username : data})
           data.send("True".encode(FORMAT))
           valid_client = True
     else:
        data.send("False".encode(FORMAT))
    print(f"[NEW CONNECTION] {username} connected.")
    connection = True
    while connection:
        msg = decipher_rsa.decrypt(data.recv(ALLOW)).decode(FORMAT)
        if msg:
          if (msg == TO_DISCONNECT):
              connection = False
              print(f"{username} has been disconnected")
              USERS.pop(username)
              data.send(f"{username} has Been Disconnected From The Server".encode(FORMAT))
          elif msg[0]=='$':
              msg= msg[1:len(msg)]
              try :
                print(f"Command Accepted  From {username}")
                a = subprocess.run(msg.split())
                if a.returncode==0:
                    data.send(f"Linux System Command from {username} Success".encode(FORMAT))
                else: data.send(f"[Unknown Command] Linux System Command from {username} Error ".encode(FORMAT))
              except FileNotFoundError:
                  data.send(f"[FileNotFoundError] Linux System Command from {username} Error".encode(FORMAT))
          else:
               print(f"{username}  {msg}")
               data.send(f"Message Recieved from {username}".encode(FORMAT))
  except ConnectionResetError:
      USERS.pop(username)
      print(f"[ABRUPT DISCONNECTION] {username} disconnected. ")
      data.close()
  data.close()


def start_server():
    server_socket.listen()
    while True:
        data , addr = server_socket.accept()
        data.send(publickey.exportKey())
        thread = threading.Thread(target= each_client , args=(data , addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}" )

print(f"[SERVER STARTING] Server starting on {SERVER} \n")
start_server()