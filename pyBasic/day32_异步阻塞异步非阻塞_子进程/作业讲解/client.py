import os
import sys
import json
import struct
import socket
def download(sk):  # 下载
    opt_dic = {'operate':'download'}
    my_send(sk,opt_dic)
    msg = my_recv(sk)
    with open(msg['filename'], 'wb') as f:
        while msg['filesize'] > 0:
            content = sk.recv(1024)
            msg['filesize'] -= len(content)
            f.write(content)

def login(sk):
    while True:
        usr = input('用户名:').strip()
        pwd = input('密 码 :').strip()
        dic = {'username': usr, 'password': pwd}
        my_send(sk, dic)
        ret = my_recv(sk)
        if ret['operate'] == 'login' and ret['result']:
            print('登录成功')
            break
        else:
            print('登录失败')
def my_recv(sk):     # 接收
    msg_len = sk.recv(4)
    dic_len = struct.unpack('i', msg_len)[0]
    msg = sk.recv(dic_len).decode('utf-8')
    msg = json.loads(msg)
    return msg


def my_send(sk,dic):   # 发送
    str_dic = json.dumps(dic)
    b_dic = str_dic.encode('utf-8')
    mlen = struct.pack('i', len(b_dic))
    sk.send(mlen)  # 4个字节 表示字典转成字节之后的长度
    sk.send(b_dic)  # 具体的字典数据



sk = socket.socket()
# sk.connect(('192.168.14.109',9012))
sk.connect(('127.0.0.1',9001))

login(sk)   # 登录
# 上传\下载
opt_lst = ['upload','download']
for index,opt in enumerate(opt_lst,1):
    print(index,opt)
num = int(input('请选择您要操作的序号 :'))
getattr(sys.modules[__name__],opt_lst[num-1])(sk)

sk.close()


