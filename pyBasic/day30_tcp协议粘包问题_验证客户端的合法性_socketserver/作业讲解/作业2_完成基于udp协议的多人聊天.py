'''
# 2. 完成基于udp协议的多人聊天
    # 自动识别用户 不能用ip和port
'''

import socket

friend_lsg = {'alex':'32', '太白':'33'}

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8086))
while True:
    msg, addr = sk.recvfrom(1500)
    msg = msg.decode('utf-8')
    name, message = msg.split('|',1)
    print('\033[1;%sm %s:%s\033[0m'%(friend_lsg.get(name, '30'),name,message))
    content = input('>>>')
    sk.sendto(content.encode('utf-8'), addr)

sk.close()