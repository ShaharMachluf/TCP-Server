# import socket module
import socket
from socket import *
import sys  # In order to terminate the program

# Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
server_port = 80 # http server
serverSocket.bind(('',server_port))
serverSocket.listen(1) # listen to 1 request at a time

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept()
    try:
        message =  connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =  f.read()
        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode('UTF-8'))
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send("404 Not Found".encode())
        # Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
