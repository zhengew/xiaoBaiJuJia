import socket
import os
import struct
import json


class Myclient:
    sk = socket.socket()
    sk.connect(('127.0.0.1', 9012))
    DOWNLOAD_PATH = '/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day30_tcp协议粘包问题_验证客户端的合法性_socketserver/作业/db'
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def login(self):
        len_name = struct.pack('i', len(self.name))
        self.sk.send(len_name)
        self.sk.send(self.name.encode('utf-8'))
        self.sk.send(self.pwd.encode('utf-8'))
        res = self.sk.recv(1024).decode('utf-8')
        res = bool(res)
        return res

    def uploads(self, filepath):
        self.filepath = filepath
        self.fname = os.path.basename(filepath)
        self.fsize = os.path.getsize(filepath)
        self.len_fname = struct.pack('i', len(self.fname))
        self.sk.send(self.len_fname)
        self.sk.send(self.fname.encode('utf-8'))
        self.sk.send(str(self.fsize).encode('utf-8'))
        with open(filepath, mode='rb') as f:
            while self.fsize > 0:
                content = f.read(1024)
                self.fsize -= len(content)
                self.sk.send(content)
        res = self.sk.recv(1024).decode('utf-8')
        return res

    def downloads(self, filename):
        self.sk.send(filename.encode('utf-8'))
        len_fsize = struct.unpack('i', self.sk.recv(4))[0]
        fsize = int(self.sk.recv(len_fsize).decode('utf-8'))
        with open(os.path.join(Myclient.DOWNLOAD_PATH, filename), mode='wb') as f:
            while fsize > 0:
                content = self.sk.recv(1024)
                fsize -= len(content)
                f.write(content)
        res = self.sk.recv(1024).decode('utf-8')
        return res



    def option(self):
        lst = [('上传', 'uploads'), ('下载', 'downloads')]
        for i in enumerate(lst, 1):
            print(i[0], i[1][0])
        opt = input('请选择: ')
        if opt.strip() == '1':
            self.sk.send('uploads'.encode('utf-8'))
            # fpath = input('文件路径:').strip()
            fpath = '/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/day30_tcp协议粘包问题_验证客户端的合法性_socketserver/作业/db/tmp.txt'
            res = self.uploads(fpath)
            print(res)
        elif opt.strip() == '2':
            self.sk.send('downloads'.encode('utf-8'))
            fname = input('文件名:').strip().lower()
            self.downloads(fname)

def main():
    obj = Myclient('test1', '123456')
    if obj.login():
        print('登陆成功')
        obj.option()
    else:
        print('用户名或密码错误')


if __name__ == '__main__':
    main()

   
