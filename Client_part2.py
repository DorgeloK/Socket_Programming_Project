from socket import *
from threading import *

serverName = "127.0.0.1"
serverPort = 35456
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


def receive():
    while 1:
        modifiedSentence = clientSocket.recv(1024)
        print(f"\nFrom Server: {modifiedSentence.decode()}")


def send():
    while 1:
        sentence = input("\nType message here: ")
        clientSocket.send(sentence.encode())


sending = Thread(target=send)
receiving = Thread(target=receive)
sending.start()
receiving.start()