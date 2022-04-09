'''
基于udp完成多人聊天的客户端
'''

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
server = ('127.0.0.1', 8086)

send_msg = input('>>>').encode('utf-8')
sk.sendto(send_msg, server)

msg = sk.recv(1024).decode('utf-8')
print(msg)

sk.close()