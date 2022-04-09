import time
import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):

        conn = self.request
        while True:
            try:
                content = conn.recv(1024).decode('utf-8')
                conn.send(content.upper().encode('utf-8'))
                time.sleep(0.5)
            except ConnectionError:
                break

server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), Myserver)
server.serve_forever()




















# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1', 9000))
# sk.listen()
#
# while True:
#     conn,_ = sk.accept()
#     while True:
#         try:
#             content = conn.recv(1024).decode('utf-8')
#             conn.send(content.upper().encode('utf-8'))
#             time.sleep(0.5)
#         except ConnectionError:
#             break

