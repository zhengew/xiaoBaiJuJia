import socket

sk = socket.socket(type=socket.SOCK_DGRAM)

name = '太白'
while True:
    content = input('>>>')
    content = '%s|%s'%(name,content)
    sk.sendto(content.encode('utf-8'), ('127.0.0.1', 9000))
    content = sk.recv(1024).decode('utf-8')
    if content.upper() == 'Q':break
    print(content)