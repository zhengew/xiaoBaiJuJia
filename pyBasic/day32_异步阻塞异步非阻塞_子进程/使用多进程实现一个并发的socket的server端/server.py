from multiprocessing import Process
import socket

def talk(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        conn.send(msg.upper().encode('utf-8'))
    conn.close()


if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 9001))
    sk.listen()

    while True:
        conn, addr = sk.accept()
        Process(target=talk, args=(conn,)).start()
    sk.close()