import socket
'''
# 参数type
    # SOCK_DGRAM UDP协议
    # SOCK_STREAM TCP协议
'''
sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9002))

while True:
    msg, addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))
    send_msg = input('>>>')
    sk.sendto(send_msg.encode('utf-8'), addr)

# udp作业
# 实现一对多聊天