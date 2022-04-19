# 多线程的socket客户端
import socket
import time
from threading import Thread

def client():
    sk = socket.socket()
    sk.connect(('127.0.0.1', 9001))

    while True:
        sk.send(b'hello')
        msg = sk.recv(1024).decode('utf-8')
        time.sleep(0.5)
        print(msg)

def main():
    for i in range(500):
        Thread(target=client).start()

if __name__ == '__main__':
    main()