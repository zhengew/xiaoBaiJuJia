'''
tcp协议的客户端
'''
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8081))

while True:
    recv_msg = sk.recv(1024).decode('utf-8')
    # recv_msg = recv_msg.
    if recv_msg.upper() == 'Q':break
    print(recv_msg)

    send_msg = input('>>>')
    sk.send(send_msg.encode('utf-8'))
    if send_msg.upper() == 'Q':break

sk.close()