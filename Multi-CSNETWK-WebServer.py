#import socket module
from socket import *
import sys # In order to terminate the program
import threading # In order to be able to accept multiple clients

def per_client(connectionSocket):
    try:
        message = connectionSocket.recv(4096).decode() #Fill in start #Fill in end 
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() #Fill in start #Fill in end
        f.close()
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #Fill in end
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
       
        connectionSocket.send("\r\n".encode())

    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())                    # Fill in
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())  # Fill in
        #Fill in end

    finally:
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
port = 3901
serverSocket.bind(('', 3901))
serverSocket.listen(5) # Queue size of 5
#Fill in end

while True:
    #Establish the connection
    print('CSNETWK Web Server is ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=per_client, args=(connectionSocket,)).start()

serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data
