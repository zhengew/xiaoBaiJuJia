import os
import socket
import struct
import os
import json

sk = socket.socket()
sk.connect(('127.0.0.1', 9001))

filepath = '/pyBasic/网络编程总结及回顾/tcp协议发送大文件到服务端/3.并发部分的概念.mp4'
filesize = os.path.getsize(filepath)
filename = os.path.basename(filepath)

file_dic = {'filename':filename, 'filesize':filesize}
file_dic = json.dumps(file_dic).encode('utf-8')
blen_dic = struct.pack('i', len(file_dic))
sk.send(blen_dic)
sk.send(file_dic)

with open(filepath, mode='rb') as f:
    while filesize >= 1024:
        content = f.read(1024)
        sk.send(content)
        filesize -= len(content)
    else:
        content = f.read()
        sk.send(content)
