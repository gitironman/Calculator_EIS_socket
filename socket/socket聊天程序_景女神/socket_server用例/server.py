import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        # 这个handle方法是每有一个客户端发起connect之后,就会执行handle
        # 在建立连接之后的所有内容都在handle中实现就可以了
        # ThreadingTCPServer帮助我们完成了tcp协议的server端的并发
        conn = self.request
        while True:
            msg = conn.recv(1024).decode('utf-8')
            print(msg)
            conn.send(msg.upper().encode('utf-8'))


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), MyServer)
server.serve_forever()

