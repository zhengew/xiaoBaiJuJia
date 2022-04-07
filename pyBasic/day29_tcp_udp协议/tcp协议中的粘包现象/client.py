import struct
import time
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9002))

# time.sleep(0.1)
# length = int(sk.recv(4).decode('utf-8'))

length = sk.recv(4)
length = struct.unpack('i', length)[0]

msg1 = sk.recv(length)
msg2 = sk.recv(1024)
print(msg1.decode('utf-8'))
print(msg2.decode('utf-8'))
''' 服务端发送两次 你好，客户端发生了粘包现象
b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xbd\xa0\xe5\xa5\xbd'
b''
'''


sk.close()