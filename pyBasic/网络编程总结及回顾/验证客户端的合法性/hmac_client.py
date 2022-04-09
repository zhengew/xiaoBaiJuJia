import socket
import hmac

sec_code = 'alex_sb'

sk = socket.socket()
sk.connect(('127.0.0.1', 9002))

rand_code = sk.recv(1024)
res = hmac.new(sec_code.encode('utf-8'), rand_code, digestmod='SHA1')
res = res.hexdigest()

sk.send(res.encode('utf-8'))
msg = sk.recv(1024).decode('utf-8')
print(msg)