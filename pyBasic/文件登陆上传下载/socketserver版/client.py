import socket
import struct
import json
import os
import sys


def send(sk, dic):
    str_dic = json.dumps(dic)
    blen_dic = struct.pack('i', len(str_dic))
    sk.send(blen_dic)
    sk.send(str_dic.encode('utf-8'))

def recv(sk):
    msg = sk.recv(4)  # 接收四字节长度
    len_dic = struct.unpack('i', msg)[0]
    dic = sk.recv(len_dic).decode('utf-8')
    dic = json.loads(dic)
    return dic

def login(sk):
    username = input('用户名:').strip()
    password = input('密码:').strip()
    dic = {'username':username, 'password':password}
    send(sk,dic)
    return recv(sk)

def download(sk):
    file_dic = recv(sk)
    with open(file_dic['filename'], mode='wb') as f:
        while file_dic['filesize'] > 0:
            content = sk.recv(1024)
            file_dic['filesize'] -= len(content)
            f.write(content)

def upload(sk):
    abs_path = r'/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/文件登陆上传下载/socketserver版/multiprocess模块'
    filename = os.path.basename(abs_path)
    filesize = os.path.getsize(abs_path)
    file_dic = {'filename': filename, 'filesize': filesize}
    send(sk, file_dic)

    with open(abs_path, 'rb') as f:
        while filesize > 0:
            content = f.read(1024)
            filesize -= len(content)
            sk.send(content)


def main():
    # 1.登陆逻辑
    sk = socket.socket()
    sk.connect(('127.0.0.1', 9010))

    ret = login(sk)
    if ret['operate'] == 'login' and ret['status']:
        opt_lst = [('上传', 'upload'), ('下载', 'download')]
        for index, opt in enumerate(opt_lst, 1):
            print(index, opt[0])
        opt = int(input('请选择:').strip())
        # 发送给服务器端执行操作
        opt_dic = {'operate':opt_lst[opt-1][1]}
        send(sk,opt_dic)
        if hasattr(sys.modules[__name__], opt_lst[opt-1][1]):
            getattr(sys.modules[__name__], opt_lst[opt-1][1])(sk)
    sk.close()

if __name__ == '__main__':
    main()