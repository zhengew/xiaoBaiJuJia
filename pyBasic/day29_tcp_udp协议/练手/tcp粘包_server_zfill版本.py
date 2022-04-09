import socket

# 版本一 通过自定义协议 设置边界，解决粘包问题
sk = socket.socket(type=socket.SOCK_STREAM)
sk.bind(('127.0.0.1', 8084))
sk.listen()

conn, addr = sk.accept() # 存储客户端和server端的连接信息
msg1 = input('>>>').encode('utf-8')
msg2 = input('>>>').encode('utf-8')
# 通过自定义协议，先发送第一条消息的长度
msg1_len = str(len(msg1)).zfill(4)
conn.send(msg1_len.encode('utf-8'))
# 第一条消息长度发送之后，再发送消息本身
conn.send(msg1)
conn.send(msg2)

conn.close()

sk.close()
