import socketserver
import struct
import hashlib
import os
import sys
import socket
import json


USER_INFO = r'/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/文件登陆上传下载/db/userinfo'
UPLOAD_PATH = r'/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/文件登陆上传下载/db/'

class Mysocketserver(socketserver.BaseRequestHandler):
    @staticmethod
    def get_md5(username, password):
        m = hashlib.md5(username.encode('utf-8'))
        m.update(password.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def recv(conn):
        msg = conn.recv(4)  # 接收四字节长度
        len_dic = struct.unpack('i', msg)[0]
        dic = conn.recv(len_dic).decode('utf-8')
        dic = json.loads(dic)
        return dic

    @staticmethod
    def send(conn, dic):
        str_dic = json.dumps(dic)
        blen_dic = struct.pack('i', len(str_dic))
        conn.send(blen_dic)
        conn.send(str_dic.encode('utf-8'))

    @staticmethod
    def login(conn):
        flag = True
        while flag:
            dic = Mysocketserver.recv(conn)
            with open(USER_INFO, mode='r', encoding='utf-8') as f:
                for info in f:
                    name, pwd = info.strip().split('|')
                    if name == dic['username'] and pwd == Mysocketserver.get_md5(dic['username'], dic['password']):
                        flag, ret = False, True
                        break
                else:
                    ret = False
            login_dic = {'operate': 'login', 'status': ret}
            Mysocketserver.send(conn, login_dic)

    @staticmethod
    def download(conn):
        abs_path = r'/Users/erwei.zheng/PycharmProjects/xiaoBaiJuJia/pyBasic/文件登陆上传下载/db/multiprocess模块'
        filename = os.path.basename(abs_path)
        filesize = os.path.getsize(abs_path)
        file_dic = {'filename': filename, 'filesize': filesize}
        Mysocketserver.send(conn, file_dic)

        with open(abs_path, 'rb') as f:
            while filesize > 0:
                content = f.read(1024)
                filesize -= len(content)
                conn.send(content)

    @staticmethod
    def upload(conn):
        file_dic = Mysocketserver.recv(conn)
        up_path = os.path.join(UPLOAD_PATH, file_dic['filename'])
        with open(up_path, mode='wb') as f:
            while file_dic['filesize'] > 0:
                content = conn.recv(1024)
                file_dic['filesize'] -= len(content)
                f.write(content)

    def handle(self):
        conn = self.request
        # 有一个客户端来连接
        Mysocketserver.login(conn)
        # 接收消息，根据用户选择进行上传/下载
        opt_lst = Mysocketserver.recv(conn)
        if hasattr(sys.modules[__name__].Mysocketserver, opt_lst['operate']):
            getattr(sys.modules[__name__].Mysocketserver,opt_lst['operate'])(conn)

        conn.close()

server = socketserver.ThreadingTCPServer(('127.0.0.1', 9010), Mysocketserver)
server.serve_forever()