'''
版本二
tcp粘包，通过struct 解决
'''
import socket
import struct

sk = socket.socket(type=socket.SOCK_STREAM)
sk.bind(('127.0.0.1', 8085))
sk.listen()

conn, addr = sk.accept()

msg1 = input('>>>').strip().encode('utf-8')
msg2 = input('>>>').strip().encode('utf-8')
# 将msg1的长度转换成byte类型， 并发送给客户端
msg1_len = struct.pack('i', len(msg1))
conn.send(msg1_len)

conn.send(msg1)
conn.send(msg2)

conn.close()
sk.close()