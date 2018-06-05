from socket import *
from threading import Thread

HOST = 'localhost'
PORT = 50000

s = socket(AF_INET,SOCK_STREAM) #create socket
s.bind((HOST,PORT))
s.listen(1) #number of connections available

connection, address = s.accept()

print ('Connection with client:', address)

while True:
    data = connection.recv(1024)
    if not data:
        break
    print ('Client: ', repr(data))

connection.close()


