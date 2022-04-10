# 1.tcp协议实现客户端发来的消息转换成大写

import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()

conn,_ = sk.accept()

content = conn.recv(1024).decode('utf-8').upper()
print(content)
