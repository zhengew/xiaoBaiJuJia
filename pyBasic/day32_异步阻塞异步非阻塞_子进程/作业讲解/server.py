import os
import sys
import json
import struct
import socket
import hashlib

# 登录成功 100 101
# 注册成功 102 103
# 上传成功 104 105
# 下载成功 106 107

def my_send(conn,dic):
    str_dic = json.dumps(dic)
    b_dic = str_dic.encode('utf-8')
    mlen = struct.pack('i', len(b_dic))
    conn.send(mlen)  # 4个字节 表示字典转成字节之后的长度
    conn.send(b_dic)  # 具体的字典数据

def download():
    abs_path = r'D:\python22期\day28 课上视频\3.网络基础概念.mp4'
    filename = os.path.basename(abs_path)
    filesize = os.path.getsize(abs_path)
    dic = {'filename': filename, 'filesize': filesize}
    my_send(conn,dic)

    with open(abs_path, mode='rb') as f:
        while filesize > 0:
            content = f.read(1024)
            filesize -= len(content)
            conn.send(content)

def my_recv(conn):
    msg_len = conn.recv(4)
    dic_len = struct.unpack('i', msg_len)[0]
    msg = conn.recv(dic_len).decode('utf-8')
    msg = json.loads(msg)
    return msg

def get_md5(username,password):
    md5 = hashlib.md5(username.encode('utf-8'))
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

def login(conn):
    flag = True
    while flag:
        # 登录
        msg = my_recv(conn)
        with open('userinfo') as f:
            for line in f:
                name, pwd = line.strip().split('|')
                if name == msg['username'] and pwd == get_md5(name, msg['password']):
                    res, flag = True, False
                    break
            else:
                res = False
            dic = {'operate': 'login', 'result': res}
            my_send(conn, dic)

# 接收
sk = socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()

conn,_ =sk.accept()
# 有了一个客户端来连接你
login(conn)
# 接收消息,根据用户的选择进行上传/下载操作
opt_dic = my_recv(conn)
if hasattr(sys.modules[__name__],opt_dic['operate']):
    getattr(sys.modules[__name__],opt_dic['operate'])()




conn.close()
sk.close()



