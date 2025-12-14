
from socket import *
from threading import *

serverName = input("Enter server IP: ")
serverPort = 35457
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("You are connected! Start chatting now")


def receive_mess():
    while 1:
        try:
            sentence = clientSocket.recv(1024)
            if sentence:
                print(sentence.decode())
        except:
            print("ERROR")
            clientSocket.close()
            break


def send_mess():
    print("Type below: ")
    while 1:
        message = input()
        clientSocket.send(message.encode())


sending = Thread(target=send_mess)
receiving = Thread(target=receive_mess)
sending.start()
receiving.start()
