'''
基于 tcp 协议，和多个客户端通信
'''
import socket

sk = socket.socket()  # 创建socket对象
sk.bind(('127.0.0.1', 8081))  # 获取系统资源
sk.listen() # 建立监听

while True:
    conn,addr = sk.accept()  # 建立连接，conn 是连接
    print('conn:', conn)
    while True:
        # 对不同的客户端进行通信，直到当前客户端断开连接
        send_msg = input('>>>')
        conn.send(send_msg.encode('utf-8'))
        if send_msg.upper() == 'Q':break
        recv_msg = conn.recv(1024).decode('utf-8')
        # recv_msg = recv_msg.decode('utf-8')
        if recv_msg.upper() == 'Q':break
        print(recv_msg)

    conn.close() # 关闭连接

sk.close() # 释放系统资源，关闭服务