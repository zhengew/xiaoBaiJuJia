import profile
import socket
import os
import json
# 发送
sk = socket.socket()

sk.connect(('127.0.0.1', 9001))

# 文件名\文件大小
abs_path = r'/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day30/tmp.txt'
filename = os.path.basename(abs_path)
filesize = os.path.getsize(abs_path)

dic = {'filename':filename, 'filesize':filesize}
str_dic = json.dumps(dic)
sk.send(str_dic.encode('utf-8'))

with open(abs_path, mode='rb') as f:
    content = f.read()
    sk.send(content)

sk.close()