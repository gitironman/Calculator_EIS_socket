import struct
import socketserver


class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        msg = '你好'.encode('utf-8') * 100
        int_num = len(msg)
        byte_num = struct.pack('i', int_num)
        conn.send(byte_num)  # 4bytes
        conn.send(msg)
        conn.send(b'world')


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), Myserver)
server.serve_forever()
