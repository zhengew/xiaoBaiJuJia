from multiprocessing import Process
import socket

def talk(conn):
    print(conn)
    while True:
        ret = conn.recv(1024).decode('utf-8')
        conn.send(ret.upper().encode('utf-8'))
    conn.close()

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 9001))
    sk.listen()

    while True:
        conn, addr = sk.accept() # 每接收一个客户端连接，就创建一个子进程
        Process(target=talk, args=(conn,)).start() # args 接收的是一个元组类型(conn,)

    sk.close()