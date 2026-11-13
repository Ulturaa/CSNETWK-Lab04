#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
#Fill in end
serverName = "Group4 Server"
port = 3901
server = socket.gethostbyname(socket.gethostname()) #Gets host IP address
address = (server,port)

server = socket.socket(socket.AF_INET, socket.SOCK_STERAM)
server.bind(address)

while True:
    #Establish the connection

    server.listen()

    print('CSNETWK Web Server is ready to serve...')
    connectionSocket, addr = server.accept()
    try:
        message = #Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = #Fill in start #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
    
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    
    except IOError:
        #Send response message for file not found
        #Fill in start
        #Fill in end
    
        #Close client socket
        #Fill in start
        
        #Fill in end
serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data
