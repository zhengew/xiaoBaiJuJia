import socket
import hashlib

secure_code = 'alex_sb'

sk = socket.socket()
sk.connect(('127.0.0.1', 9001))

rand_code = sk.recv(1024)

sha = hashlib.sha1(secure_code.encode('utf-8'))
sha.update(rand_code)
res = sha.hexdigest()

sk.send(res.encode('utf-8'))

msg = sk.recv(1024).decode('utf-8')
print(msg)

