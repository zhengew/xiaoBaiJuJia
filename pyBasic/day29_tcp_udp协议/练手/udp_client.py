import socket

sk = socket.socket(type = socket.SOCK_DGRAM) # udp协议
server = ('127.0.0.1', 8082)

while True:
    send_msg = input('>>>')
    if send_msg.upper() == 'Q':break
    sk.sendto(send_msg.encode('utf-8'), server)
    recv_msg = sk.recv(1024).decode('utf-8')
    if recv_msg.upper() == 'Q':break
    print(recv_msg)