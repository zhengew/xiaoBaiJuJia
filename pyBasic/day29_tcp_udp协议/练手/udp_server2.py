'''
实现一收一发的通信
'''

import socket

sk = socket.socket(type=socket.SOCK_DGRAM) # udp协议
sk.bind(('127.0.0.1', 8083)) # 申请服务器资源

while True:
    msg, addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    send_msg = input('>>>')
    sk.sendto(send_msg.encode('utf-8'),addr) # 向客户端发送消息

