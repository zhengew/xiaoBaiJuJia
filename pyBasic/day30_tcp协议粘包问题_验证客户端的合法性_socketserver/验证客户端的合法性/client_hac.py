'''验证客户端的合法性
hmac
'''

import socket
import hmac
import os
secret_code = b'alex_sb'

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

rand = sk.recv(1024)
res = hmac.new(secret_code, rand, digestmod='MD5')
res = res.digest()
sk.send(res)

msg = sk.recv(1024).decode('utf-8')
print(msg)
