'''
# 2. 完成基于udp协议的多人聊天
    # 自动识别用户 不能用ip和port
'''

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 8086))

msg, addr = sk.recvfrom(1024)
print(msg.decode('utf-8'), addr)
sed_msg = input('>>>').encode('utf-8')
sk.sendto(sed_msg, addr)

sk.close()