import socket
import struct

sk = socket.socket()
sk.connect(('127.0.0.1', 9010))
while True:
    msg = input('>>>')
    # # 此处返回字节的长度，不要用字符
    lenth = struct.pack('i', len(msg.encode('utf-8')))
    sk.send(lenth)
    # 发送的时候，要把字符encode成字节
    sk.send(msg.encode('utf-8'))
    if msg.upper() == 'Q': break
    # 接收的时候要把字节decode成字符
    content = sk.recv(1024).decode('utf-8')
    if content.upper() == 'Q':break
    print(content)

sk.close()

