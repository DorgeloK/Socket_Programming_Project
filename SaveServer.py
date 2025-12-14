from socket import *
from threading import *
import random

clients = []

def handle_c(conn, addr):
    global clients
    addr = random.sample(range(1, 100), 1)
    print(f'{addr} has joined the chat')
    while 1:
        try:
            sentence = conn.recv(1024).decode()
            if not sentence:
                break

            print(f'{addr}: {sentence}')

            # Broadcast message to all other clients
            for c in clients:
                if c != conn:
                    try:
                        c.send(f'{addr}: {sentence}'.encode())
                    except:
                        clients.remove(c)
                        c.close()
        except:
            break

    print(f'{addr} has left the chat')
    clients.remove(conn)
    conn.close()

def run_s():
    global clients

    serverPort = 35457
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverName = input("Enter server IP: ")
    serverSocket.bind((serverName, serverPort))
    serverSocket.listen(10)

    print("Server is listening...")

    while 1:
        conn, addr = serverSocket.accept()
        clients.append(conn)
        thread = Thread(target=handle_c, args=(conn, addr))
        thread.start()

run_s()
