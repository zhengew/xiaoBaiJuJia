# 基于tcp协议的通信
import socket

sk = socket.socket() # 创建socket对象
sk.bind(('127.0.0.1', 9000)) # 给server端绑定一个ip和端口
sk.listen() # 建立监听

conn, addr = sk.accept() # 建立连接，conn是连接
conn.send('你好'.encode('utf-8')) # 服务端发送 一条消息
msg = conn.recv(1024) # 服务端接收一次消息，1024个字节
print(msg.decode('utf-8'))

conn.close() # 关闭连接

sk.close() # 关闭服务

