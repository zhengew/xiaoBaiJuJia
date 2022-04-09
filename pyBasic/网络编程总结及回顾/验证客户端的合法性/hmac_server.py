import socket
import hmac
import os

sec_code = 'alex_sb'

sk = socket.socket()
sk.bind(('127.0.0.1', 9002))
sk.listen()

conn,_ = sk.accept()

rand_code = os.urandom(32)
conn.send(rand_code)
res = hmac.new(sec_code.encode('utf-8'), rand_code, digestmod='SHA1')
res = res.hexdigest()

client_res = conn.recv(1024).decode('utf-8')
if client_res == res:
    print('合法客户端')
    conn.send(b'hello')
else:
    print('非法客户端')
    conn.close()