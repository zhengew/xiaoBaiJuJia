import socket
import struct

sk = socket.socket()
sk.bind(('127.0.0.1', 9010))
sk.listen()

while True:
    conn, addr = sk.accept()
    while True:
        msg_len = conn.recv(4)
        lenth = struct.unpack('i', msg_len)[0]
        msg = conn.recv(lenth).decode('utf-8')
        if msg.upper() == 'Q':break
        print(msg)
        content = input('>>>')
        conn.send(content.encode('utf-8'))
        if content.upper() == 'Q':break
    conn.close()

sk.close()