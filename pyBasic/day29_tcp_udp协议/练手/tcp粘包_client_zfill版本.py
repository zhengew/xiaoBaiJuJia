import socket

# 版本一 通过自定义协议 设置边界，解决粘包问题

sk = socket.socket(type=socket.SOCK_STREAM)
sk.connect(('127.0.0.1', 8084))
# 先接收服务端自定义协议，第一条消息的长度
length = int(sk.recv(4).decode('utf-8'))
# 再按照接收的长度接收第一条消息
msg1 = sk.recv(length).decode('utf-8')
msg2 = sk.recv(1024).decode('utf-8')
print(msg1)
print(msg2)

sk.close()