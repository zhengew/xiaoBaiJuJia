import socket
import json
# 接收
sk = socket.socket()
sk.bind(('127.0.0.1', 9001))
sk.listen()

conn,_ = sk.accept()

msg = conn.recv(1024).decode('utf-8')
msg = json.loads(msg)
print(msg)

with open(msg['filename'], 'wb') as f:
    content = conn.recv(msg['filesize'])
    print('--->', len(content))
    f.write(content)

conn.close()
sk.close()