import socket

sk = socket.socket(type=socket.SOCK_DGRAM)

while True:
    sk.sendto(b'hello', ('127.0.0.1', 9003))
    content = sk.recv(1024).decode('utf-8')
    if content.upper() == 'Q':break

sk.close()