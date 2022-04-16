import socket
print(socket.socket)          # 在patch all之前打印一次
from gevent import monkey    # gevent 如何检测是否能规避某个模块的io操作呢?
monkey.patch_all()
import socket
import gevent
print(socket.socket)           # 在patch all之后打印一次,如果两次的结果不一样,那么就说明能够规避io操作

def func(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        conn.send(msg.upper().encode('utf-8'))

sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()


while True:
    conn,_ = sk.accept()
    gevent.spawn(func,conn)
