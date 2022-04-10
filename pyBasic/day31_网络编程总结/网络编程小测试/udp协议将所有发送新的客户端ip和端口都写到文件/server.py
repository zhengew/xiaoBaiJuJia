# 2.udp协议将所有发送新的客户端ip和端口都写到文件

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9003))


while True:
    msg, addr = sk.recvfrom(1024)
    with open('addr.txt', mode='a', encoding='utf-8') as f:
        f.seek(0, 2)
        f.write(addr[0] + '|' + str(addr[1]) + '\n')

    sk.sendto('Q'.encode('utf-8'), addr)