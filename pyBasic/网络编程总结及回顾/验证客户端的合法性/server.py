import socket
import hashlib
import os

secure_code = 'alex_sb'

sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()

conn,_ = sk.accept()

rand_code = os.urandom(32)
conn.send(rand_code)

# 服务端私钥与公钥加密
sha = hashlib.sha1(secure_code.encode('utf-8'))
sha.update(rand_code)
res = sha.hexdigest()
# 接收服务端私钥公钥加密后的结果
client_res = conn.recv(1024).decode('utf-8')

if client_res == res:
    print('合法客户端')
    conn.send(b'hello')
else:
    print('非法客户端')
    conn.close()




