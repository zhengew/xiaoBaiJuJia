import socket
sk = socket.socket()
sk.connect(('127.0.0.1',9001))


while True:
    msg = sk.recv(1024)
    msg2 = msg.decode('utf-8')
    if msg2.upper() == 'Q':
        break
    print(msg2)
    send_msg = input('>>>')
    sk.send(send_msg.encode('utf-8'))
    if send_msg.upper() == 'Q':
        break
sk.close()