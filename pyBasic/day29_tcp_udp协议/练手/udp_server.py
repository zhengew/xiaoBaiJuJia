'''
简单的udp协议
'''
import socket

sk = socket.socket(type=socket.SOCK_DGRAM) # ucp协议
sk.bind(('127.0.0.1', 8082))

while True:
    msg, addr = sk.recvfrom(1024)
    print(addr)
    print(msg.decode('utf-8'))
    send_msg = input('>>>')
    sk.sendto(send_msg.encode('utf-8'),addr)