from socket import *

serverPort = 35456
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print(f'Received message: {sentence.decode()}')
    words = input("Input here: ")
    connectionSocket.send(words.encode())
    connectionSocket.close()