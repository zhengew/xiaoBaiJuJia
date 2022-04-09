'''
# 1.基于tcp协议完成登陆认证
    # 客户端输入用户名密码
    # 发送到服务端
    # 服务端认证
    # 发送结果到客户端
'''
import socket
import struct


USERS = {'test1':'123456',
         'test2':'123456'}

def auth(name, pwd):
    if name in list(USERS.keys()) and pwd == USERS[name]:
        return True
    else:
        return False

def main():
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8085))
    sk.listen()
    while True:
        conn, addr = sk.accept()
        print(conn, addr)
        lenth = struct.unpack('i', conn.recv(4))[0]
        uname = conn.recv(lenth).decode('utf-8')
        pwd = conn.recv(1024).decode('utf-8')

        conn.send(str(auth(uname,pwd)).encode('utf-8'))
        conn.close()

    sk.close()

if __name__ == '__main__':
    main()
