import socket

sk = socket.socket()            # 创建一个server端的对象
sk.bind(('127.0.0.1',9000))     # 给server端绑定一个地址
sk.listen() # 监听               # 开始监听

conn, addr = sk.accept()        # 建立连接 conn 是连接
conn.send(b'hello')
msg = conn.recv(1024)
print(msg)
conn.close()

sk.close()