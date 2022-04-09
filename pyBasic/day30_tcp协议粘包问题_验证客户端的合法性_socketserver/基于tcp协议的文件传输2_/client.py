import profile
import socket
import os
import json
# 发送
sk = socket.socket()

sk.connect(('127.0.0.1', 9001))

# 文件名\文件大小
abs_path = r'/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day30/2.tcp协议完成文件上传.mp4'
filename = os.path.basename(abs_path)
filesize = os.path.getsize(abs_path)

dic = {'filename':filename, 'filesize':filesize}
str_dic = json.dumps(dic)
sk.send(str_dic.encode('utf-8')) # 次数有可能跟下面的send发生粘包

with open(abs_path, mode='rb') as f:
    while filesize > 0:
        content = f.read(1024)
        filesize -= len(content)
        sk.send(content)
sk.close()