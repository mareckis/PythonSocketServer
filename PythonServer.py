from socket import *
import threading
from _thread import *

def ClientHandlingFunction(client_socket,client_address):

    print("Client connected: ", client_address)

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        else:
            print ("Client {client_address} message: {}".format(client_address,data))
            client_socket.send()
    client_socket.close()

def Main():
    HOST = 'localhost'
    PORT = 50000

    s = socket(AF_INET,SOCK_STREAM) #create socket
    s.bind((HOST,PORT))
    s.listen(5) #number of connections available

    print ("Server ok")

    while True:
        print ("Listening")

        client_socket, client_address = s.accept()
        start_new_thread(ClientHandlingFunction,(client_socket,client_address))

    s.close()

if __name__ == "__main__":
    Main()
