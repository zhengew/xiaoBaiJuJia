''' udp协议的多人多次通信'''

import socket

friend_lst = {'太白':'32', 'alex':'33'}

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9000))
while True:
    msg, addr = sk.recvfrom(1024)
    msg = msg.decode('utf-8')
    print(msg, addr)
    name, content = msg.split('|')
    print('\033[1;%sm %s:%s\033[0m' % (friend_lst.get(name, '30'), name, content))
    content = input('>>>').encode('utf-8')
    sk.sendto(content, addr)


