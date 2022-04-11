import socket
from multiprocessing import Process
sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()

conn, addr = sk.accept()
while True:
    msg = conn.recv(1024).decode('utf-8')
    ret = msg.upper().encode('utf-8')
    conn.send(ret)

conn.close()
sk.close()

