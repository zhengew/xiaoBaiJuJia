# 1. 登陆 + 文件下载
    # 用户必须登陆才能下载
    # 用户是否登陆应该记录在服务器端
    # 并且用户可以自己选择上传或者下载

# user保存用户名密码和登陆状态，0-logout 1-login

import socketserver
import os
import struct
import json

USER_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db', 'user')


class Myserver(socketserver.BaseRequestHandler):
    file_dic = {}
    def login(self, name, pwd):
        self.name = name
        self.pwd = pwd
        with open(USER_PATH, mode='r', encoding='utf-8') as f:
            flag = False
            for info in f:
                uname, upwd = info.strip().split('|')
                if self.name == uname and self.pwd == pwd:
                    flag =  True
                    break
        return flag
    # 相对与客户端的上传，服务端就是下载
    # def downloads(self):
    #     pass

    # def uploads(self):
    #     len_fname = struct.unpack('i', self.recv(4))[0]
    #     fname = self.conn.recv(len_fname).decode('utf-8')
    #     fsize = self.conn.recv(1024).decode('utf-8')
    #     Myserver.file_dic.setdefault(fname, int(fsize))
    #     with open(fname, mode='wb') as f:
    #         while Myserver.file_dic[fname] > 0:
    #             content = self.conn.recv(1024)
    #             Myserver.file_dic[fname] -= len(content)
    #             f.write(content)
    #     self.conn.send('上传成功'.encode('utf-8'))


    def handle(self) -> None:
        self.conn = self.request
        while True:
            try:
                len_cname = struct.unpack('i', self.conn.recv(4))[0]
                cname = self.conn.recv(len_cname).decode('utf-8')
                cpwd = self.conn.recv(1024).decode('utf-8')
                print(cname, cpwd)

                loginstatus = self.login(cname,cpwd)
                self.conn.send(str(loginstatus).encode('utf-8'))
                if loginstatus:
                    print('开始执行login')
                    # 当登陆成功的时候，我要接收客户端发过来的下一步请求是什么？
                    # 如果是 uploads 我就执行 服务端的uploads代码
                    # 如果是 downloads 我就执行服务端的 downloads 代码
                    # 所以登陆成功之后，现需先recv客户端的下一步消息
                    next_opt = self.conn.recv(1024).decode('utf-8')
                    print(next_opt)
                    if next_opt.lower() == 'uploads':
                        # 上传逻辑
                        len_fname = struct.unpack('i', self.conn.recv(4))[0]
                        fname = self.conn.recv(len_fname).decode('utf-8')
                        fsize = self.conn.recv(1024).decode('utf-8')
                        Myserver.file_dic.setdefault(fname, int(fsize))
                        with open('file_dic.txt', mode='a', encoding='utf-8') as f:
                            f.seek(0,2)
                            f.write(fname+'|'+fsize+'\n')
                        with open(fname, mode='wb') as f:
                            while Myserver.file_dic[fname] > 0:
                                content = self.conn.recv(1024)
                                Myserver.file_dic[fname] -= len(content)
                                f.write(content)
                        self.conn.send('上传成功'.encode('utf-8'))
                    # 下载这里有问题
                    # elif next_opt.lower() == 'downloads':
                    #     fname = self.conn.recv(1024).decode('utf-8')
                    #     print(fname)
                    #     file_dic = {}
                    #     with open('file_dic.txt', mode='r', encoding='utf-8') as f:
                    #         for info in f:
                    #             name, size = info.strip().split('|')
                    #             if name == fname:
                    #                 file_dic.setdefault(fname, int(size))
                    #                 break
                    #     print(file_dic)
                    #     if fname in list(file_dic.keys()):
                    #         self.fsize = file_dic[fname]
                    #         len_fsize = struct.pack('i', len(str(self.fsize)))
                    #         self.conn.send(len_fsize)
                    #         self.conn.send(str(self.fsize).encode('utf-8'))
                    #
                    #         with open(fname, mode='rb') as f:
                    #             while file_dic[fname] > 0:
                    #                 content = f.read(1024)
                    #                 file_dic[fname] -= len(content)
                    #                 self.conn.send(content)
                    #         self.conn.send('下载成功'.encode('utf-8'))
                    #     # else:
                    #     #     self.conn.send(f'{fname}文件不存在'.encode('utf-8'))



            except ConnectionError:
                self.conn.close()

server = socketserver.ThreadingTCPServer(('127.0.0.1', 9012), Myserver)
server.serve_forever()












