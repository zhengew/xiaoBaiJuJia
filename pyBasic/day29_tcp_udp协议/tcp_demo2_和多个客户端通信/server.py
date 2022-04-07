import socket
sk = socket.socket()
sk.bind(('127.0.0.1',9001))   # 申请操作系统的资源
sk.listen()

while True: # 为了和多个客户端握手
    conn,addr = sk.accept() # 能够和多个客户端进行握手了
    print('conn : ',conn)
    while True:
        send_msg = input('>>>')
        conn.send(send_msg.encode('utf-8'))
        if send_msg.upper() == 'Q':
            break
        msg = conn.recv(1024).decode('utf-8')
        if msg.upper() == 'Q':
            break
        print(msg)
    conn.close()    # 挥手 断开连接

sk.close()      # 归还申请的操作系统的资源


# str -encode('utf-8')-> bytes
# str -encode('gbk')-> bytes
# '你' 字符
# utf-8  b'181921'      b'181921' -decode('utf-8')-> 你
# gbk    b'17210'       b'17210'  -decode('gbk')  -> 你

# 作业
# 聊天这个得会背诵
# 基于tcp协议的文件传输