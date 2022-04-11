import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9001))

while True:
    sk.send(b'hello')
    msg = sk.recv(1024).decode('utf-8')
    print(msg)

sk.close()