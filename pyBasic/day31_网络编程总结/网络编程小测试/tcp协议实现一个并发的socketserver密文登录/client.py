import socket
import hashlib
import struct

sk = socket.socket()
sk.connect(('127.0.0.1', 9009))

while True:
    name = input('用户名:').strip()
    pwd = input('密码:').strip()

    sha = hashlib.sha1(name.encode('utf-8'))
    sha.update(pwd.encode('utf-8'))
    sha = sha.hexdigest()
    # 发送服务端用户名和密码
    name_len = struct.pack('i', len(name.encode('utf-8')))
    sk.send(name_len) # 用户名长度
    sk.send(name.encode('utf-8'))
    sk.send(sha.encode('utf-8'))
    result = sk.recv(1024).decode('utf-8')
    if result.upper() == 'Q':
        break
    else:
        print(result)
sk.close()


