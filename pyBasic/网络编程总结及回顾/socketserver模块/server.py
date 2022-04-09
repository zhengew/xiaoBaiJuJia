import socketserver
import time

class Mysocket(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            try:
                content = conn.recv(1024).decode('utf-8')
                conn.send(content.upper().encode('utf-8'))
                time.sleep(0.5)
            except ConnectionError:
                conn.clse()


sever = socketserver.ThreadingTCPServer(('127.0.0.1', 9003), Mysocket)
sever.serve_forever()










# # socket 原生版本
# import socket
# sk = socket.socket()
# sk.bind(('127.0.0.1', 9001))
# sk.listen()
# while True:
#     conn,_ = sk.accept()
#     while True:
#         content = conn.recv(1024).decode('utf-8')
#         print(content)
#         msg = input('>>>')
#         conn.send(msg.encode('utf-8'))
#     conn.clse()
#
# sk.close()
