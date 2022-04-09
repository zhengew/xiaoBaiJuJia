''' 客户端
# 3.基于tcp协议完成一个文件的上传
    # 小文件
    # 进阶 大文件
'''
import socket
import struct

def recv_file(path, msg):
    with open(path, mode='a', encoding='utf-8') as f:
        f.seek(0, 2)
        f.write(msg+'\n')
        f.flush()

def main():
    sk = socket.socket()
    sk.connect(('127.0.0.1', 8089))
    flag = 0
    path = 'client_info'

    if flag == 0:
        lenth = struct.unpack('i', sk.recv(4))[0]
        print(lenth)
        flag += 1
    msg = sk.recv(lenth).decode('utf-8')
    # while True:
        # if sk.recv(1024).decode('utf-8').upper() == 'Q':
        #     print(111)
        #     break

            # print(msg.decode('utf-8'))
        #     flag += 1
        # print(sk.recv(1024).decode('utf-8'))

    sk.close()
if __name__ == '__main__':
    main()