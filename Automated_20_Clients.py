import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import threading
from random import randrange

ALLOW = 2048
PORT = 6666
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
TO_DISCONNECT = '!DISCONNECT!'
i=.000001
client_sockets = []

f=open("message.txt")
a=f.readlines()
l=len(a)

def sendMessage(data, name,cipher_rsa):
 for i in range (2):
    n = randrange(0,l)
    z = a[n]
    if z!='\n':
       z=z.replace('\n',"")
       data.send(cipher_rsa.encrypt(z.encode('utf-8')))
       print(f"{name} : {z} ")
       command_ack = data.recv(1024).decode(FORMAT)
       print(command_ack)
 data.send(cipher_rsa.encrypt("!DISCONNECT!".encode('utf-8')))
 data.close()

def get_clients():
  for i in range(20):
    client_sockets.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    client_sockets[i].connect(ADDR)
    publicKey = client_sockets[i].recv(1024)
    publicKey = RSA.importKey(publicKey)
    cipher_rsa = PKCS1_OAEP.new(publicKey)
    client_sockets[i].send(cipher_rsa.encrypt(("Client"+str(i+1)).encode('utf-8')))
    if client_sockets[i].recv(32).decode(FORMAT):
      thread = threading.Thread( target= sendMessage , args= (client_sockets[i],"Client"+str(i+1),cipher_rsa))
      thread.start()

get_clients()