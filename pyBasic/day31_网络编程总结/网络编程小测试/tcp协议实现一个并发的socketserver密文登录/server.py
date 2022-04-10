# 3.tcp协议实现一个并发的socketserver密文登录
import socketserver
import struct
SOAT = 'test'
import hashlib
USER = {'name':'1196f198de1099f806df54d4140de25d3902095e'}
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            try:
                name_len = struct.unpack('i', conn.recv(4))[0]
                client_name = conn.recv(name_len).decode('utf-8')
                client_sha = conn.recv(1024).decode('utf-8')
                client_sha_soat = hashlib.sha1(SOAT.encode('utf-8'))
                client_sha_soat.update(client_sha.encode('utf-8'))
                client_sha_soat = client_sha_soat.hexdigest()

                flag = False
                with open('smteller.txt', mode='r', encoding='utf-8') as f:
                    for info in f:
                        name, pwd = info.strip().split('|')
                        if name == client_name and client_sha_soat == pwd:
                            flag = True
                            break
                if flag:
                    conn.send(b'hello')
                else:
                    conn.send('Q'.encode('utf-8'))

            except ConnectionError:
                conn.close()

server = socketserver.ThreadingTCPServer(('127.0.0.1', 9009), Myserver)
server.serve_forever()
