# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9001))
# sk.listen()
#
# conn,addr = sk.accept()
# conn.send('你好'.encode('utf-8'))
# conn.send('你好'.encode('utf-8'))
# conn.close()
#
# sk.close()



# 粘包现象
# 只出现在tcp协议中，因为tcp协议 多条消息之间没有边界，并且还有一大堆优化算法
# 发送端：两条消息很短，发送的时间间隔也非常短
# 接收端：多条消息由于没有及时接收，而在接收方的缓存端堆在一起导致的粘包

# 解决粘包问题的本质：设置边界


# # 自定义协议解决粘包显现
# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9002))
# sk.listen()
#
# conn,addr = sk.accept()
# msg1 = input('>>>').encode('utf-8')
# msg2 = input('>>>').encode('utf-8')
# num = str(len(msg1)) # 6
# # 从左边补充0，填充到当前的字符串，长度为4
# ret = num.zfill(4) # 0006 通过自定义协议，限制第一次消息的长度，客户端再按照指定长度解析数据
# print(ret)
# conn.send(ret.encode('utf-8'))
# conn.send(msg1)
# conn.send(msg2)
# conn.close()
#
# sk.close()


''' 用 struct 模块解决粘包问题 '''

import socket
import struct

sk = socket.socket()
sk.bind(('127.0.0.1',9002))
sk.listen()

conn,addr = sk.accept()
msg1 = input('>>>').encode('utf-8')
msg2 = input('>>>').encode('utf-8')

blen = struct.pack('i', len(msg1))
conn.send(blen)

conn.send(msg1)
conn.send(msg2)
conn.close()

sk.close()











