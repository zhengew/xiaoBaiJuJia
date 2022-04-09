import contextlib
import socket
import json
import struct
# 接收
sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()

conn,_ = sk.accept()

msg_len = conn.recv(4) # 先接收字典的字节长度
dic_len = struct.unpack('i', msg_len)[0] # 在unpack
msg = conn.recv(dic_len).decode('utf-8') # 在接收实际字典长度的数据
msg = json.loads(msg) # 在通过json load回来
print(msg)

with open(msg['filename'], 'wb') as f:
    while msg['filesize'] > 0:
        content = conn.recv(1024)
        msg['filesize'] -= len(content) # -len(content) 解决丢包问题
        f.write(content)
        print('--->', len(content))

conn.close()
sk.close()

# dir
    # file1
    # file2
    # file3