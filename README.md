# CLI-Chatbox
send text messages and command line instructions 
Follow these instructions to run the server-client CLI chat interface(some instructions may have sub points)

1) open Terminal window then install pycryptodome 3.9.7 :  (this is to in-corporate the RSA module library, for secure channel communication)
               
      a)--  pip install pycryptodome  --  type this instruction in the cmd line
    
      b)If you have 'PyCrypto' already installed then you should install pycrypotodomex
             --pip install pycryptodomex-- this is a library independent of the old PyCrypto(if you had that originally only)
               this is so that pycrypto and pycryptodome can co-exisit in your system
               (!!REMEMBER step 1b is only for those who had PyCrypto lib installed)

2) on the Terminal navigate to file(server.py , client.py etc) directory(i.e the folder which contains these files)
3) once you are in the directory run the command 
               -- python server.py --  to RUN the server scrypt on the TERMINAL of your system
           REMEMBER to only run the server on command line and not in any python IDE as the linux commands send from the clients will only run/function if its a terminal
4)Then you can run the client scrypt on the terminal by the command  [python client.py] or any python IDE's as you wish
5)then you will be prompted to type a username which will be unique for you 
6)now you are free to type the text in any format you wish as prompet by the client console, this text will go directly to the server via RSA encryption . eg hellow, hi from client etc.
  you will be given an ACKNOWLEDGEMENT message back from the Server as "Message Recieved form {user} " as a confirmation to your text send.
7)IMPORTANT : if you wish to type a LINUX COMMAND then add a '$' prefix before your command. Eg. $ls -a , $pwd etc.
  you will get an ACKNOWLEDGEMENT message back from the server as "Linux System Command from {username} Success" if your given command was a valid linux command or you will get a NO-ACKNOWLEDGEMENT message saying "Linux System Command from {username} Error"
8)you can run client.py script on any device connected in the same local network (following step 4 onwards)  and give each a differnt user name to make them all communicate with the server individually and securly, also you can
   give individual linux command to the server system (following step 7) from each device connected(devices running client.py and connected to the local network)
9)if you wish to log out from the connection to the server typr the text : !DISCONNECT! 

10)if you wish to see the running of an automated 20 client to 1 server system run Automate_20_Client.py file on the terminal --python Automate_20_Client.py-- or just run it through any python IDE.
  REMEMBER : server.py(step 3) should be running before running any client scrypts (client.py , Automate_20_Client.py)
   these 20 clients will run random texts/linux commands from the message.txt file and automatically log out from the server after completion.



FEATURES

RSA secure transmission
run linux commands easily with just adding '$' at the begining
Clear loggings of all Errors, message confirmation, linux command implementation on both client and server side is available.
in case of abrubt disconnection (ie, without logging off) the user is automatically removed from clients
fixed bugs of sending blank username or text or command when prompted.
Unique username for each client
