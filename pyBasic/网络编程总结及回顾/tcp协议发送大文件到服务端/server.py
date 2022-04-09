''' tcp 协议发送小文件到服务端 '''
import socket
import struct
import json

sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()

conn,_ = sk.accept()

blen_dic = conn.recv(4)
blen_dic = struct.unpack('i', blen_dic)[0]
file_dic = conn.recv(blen_dic).decode('utf-8')
file_dic = json.loads(file_dic)

with open(file_dic['filename'], mode='wb') as f:
    while file_dic['filesize'] > 0:
        content = conn.recv(1024)
        file_dic['filesize'] -= len(content)
        f.write(content)
        print('while==>', len(content))

conn.close()
sk.close()



