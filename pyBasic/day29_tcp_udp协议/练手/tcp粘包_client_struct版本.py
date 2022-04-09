'''
版本二
tcp粘包，通过struct 解决
'''
import socket
import struct

sk = socket.socket(type=socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 8085))
# 将msg1长度由byte类型转换成10进制数字
lenth = struct.unpack('i', sk.recv(4))[0]

msg1 = sk.recv(lenth).decode('utf-8')
msg2 = sk.recv(1024).decode('utf-8')
print(msg1)
print(msg2)