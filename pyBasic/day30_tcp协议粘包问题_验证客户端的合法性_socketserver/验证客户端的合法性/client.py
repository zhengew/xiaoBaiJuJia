import socket
import os
import hashlib
secret_key = b'alex_sb'

sk = socket.socket()
sk.connect(('127.0.0.1', 9001))

# 接收客户端发送的随机字符串
rand = sk.recv(32)
# 根据发送的随机字符串 + secret_key 进行摘要
sha = hashlib.sha1(secret_key)
sha.update(rand)
res = sha.hexdigest()
# 摘要结果发送会server端
sk.send(res.encode('utf-8'))
# 继续和server端进行通信
msg = sk.recv(1024)
print(msg)