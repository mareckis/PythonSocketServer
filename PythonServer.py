from socket import *
from threading import Thread

host = "127.0.0.1"
port = 8000

s = socket(AF_INET,SOCK_STREAM) #create socket
s.bind((host,port))
s.listen(1) #number of connections available

connection_id, ip_address = s._accept()

print ('Connection with client:', ip_address)


