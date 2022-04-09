'''验证客户端的合法性
hmac
'''

import socket
import hmac
import os
secret_code = b'alex_sb'

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

conn, addr = sk.accept()
rand = os.urandom(32)
conn.send(rand)
res = hmac.new(secret_code, rand, digestmod='MD5')
res = res.digest()
client_res = conn.recv(1024)
if res == client_res:
    print('合法客户端')
    conn.send(b'hello')
else:
    conn.close()

sk.close()


