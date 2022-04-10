import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9001))

sk.send('hello'.encode('utf-8'))