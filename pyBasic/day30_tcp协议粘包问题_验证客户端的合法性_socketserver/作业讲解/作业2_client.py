'''
基于udp完成多人聊天的客户端
'''

import socket
name = '大壮'
sk = socket.socket(type=socket.SOCK_DGRAM)

while True:
    content = input('>>>')
    if content.upper() == 'Q': break
    content = '%s|%s' %(name,content)
    sk.sendto(content.encode('utf-8'), ('127.0.0.1', 8086))
    msg = sk.recv(1024).decode('utf-8')
    print(msg)
    if msg.upper() == 'Q':break
sk.close()