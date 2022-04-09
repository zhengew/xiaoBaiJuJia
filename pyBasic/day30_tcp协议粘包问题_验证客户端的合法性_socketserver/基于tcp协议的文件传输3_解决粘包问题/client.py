import profile
import socket
import os
import json
import struct
# 发送
sk = socket.socket()

sk.connect(('127.0.0.1', 9001))

# 文件名\文件大小
abs_path = r'/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day30/tmp.txt'
filename = os.path.basename(abs_path)
filesize = os.path.getsize(abs_path)

dic = {'filename':filename, 'filesize':filesize}
str_dic = json.dumps(dic)
b_dic= str_dic.encode('utf-8')
m_len = struct.pack('i',len(b_dic))
sk.send(m_len) # 4个字节，表示字典转成字节之后的长度
sk.send(b_dic) # 具体的字典

# 由于第一次发送和第二次发送可能存在粘包问题，所以要先发送字典字节长度

with open(abs_path, mode='rb') as f:
    while filesize > 0:
        content = f.read(1024)
        filesize -= len(content)
        sk.send(content)
sk.close()



# 作业，远程文件的下载
# 先登陆
# 能上传到固定目录、下载(从指定文件夹下选择文件)