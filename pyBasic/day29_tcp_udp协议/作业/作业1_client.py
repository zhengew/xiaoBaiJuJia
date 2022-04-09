import socket
import struct

sk = socket.socket()
sk.connect(('127.0.0.1', 8085))

def login():
    while True:
        name = input('用户名：').strip().encode('utf-8')
        name_len = struct.pack('i', len(name))
        sk.send(name_len)
        pwd = input('密码:').strip().encode('utf-8')
        sk.send(name)
        sk.send(pwd)
        return sk.recv(1024).decode('utf-8')
        sk.close()

def main():
    print(login())
if __name__ == '__main__':
    main()