# 基于tcp协议的通信
import socket

sk = socket.socket() # 创建一个客户端对象
sk.connect(('127.0.0.1', 9000)) # 连接服务端的ip和短裤

msg = sk.recv(1024).decode('utf-8') # 客户端接收消息
print(msg)
sk.send('哈喽'.encode('utf-8')) # 客户端发送消息

sk.close() # 客户端断开连接