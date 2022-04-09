''' 服务端
# 3.基于tcp协议完成一个文件的上传
    # 小文件
    # 进阶 大文件
'''
import os
import socket
import struct
import pickle
import json

def send_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        for info in f:
            yield info.strip()


def main():
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8089))
    sk.listen()
    path = 'info'
    conn, addr = sk.accept()
    flag = 0
    for info in send_file(path):
        if flag == 0:
            lenth = struct.pack('i', len(info))
            conn.send(lenth)
            conn.send(info.encode('utf-8'))
            flag += 1
        else:
            conn.send(info.encode('utf-8'))
    conn.send('Q'.encode('utf-8'))
    conn.close()
    sk.close()
    # for i in send_file('info'):
    #     print(i.strip())

if __name__ == '__main__':
    main()