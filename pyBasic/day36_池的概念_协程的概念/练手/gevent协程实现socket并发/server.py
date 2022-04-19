# gevent协程实现socket并发的服务端
import socket
from gevent import monkey
monkey.patch_all()
import gevent


def func(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        conn.send(msg.upper().encode('utf-8'))

def main():
    sk = socket.socket()
    sk.bind(('127.0.0.1', 9001))
    sk.listen()

    while True:
        conn, _ = sk.accept()
        gevent.spawn(func, conn)

if __name__ == '__main__':
    main()