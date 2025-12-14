from socket import *
from threading import *

serverPort = 35456
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("127.0.0.1", serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
connectionSocket, addr = serverSocket.accept()


def receive():
    while 1:
        sentence = connectionSocket.recv(1024)
        print(f'\nReceived message: {sentence.decode()}')


def sending():
    while 1:
        words = input("\nInput here: ")
        connectionSocket.send(words.encode())


sending = Thread(target=sending)
receiving = Thread(target=receive)
receiving.start()
sending.start()
