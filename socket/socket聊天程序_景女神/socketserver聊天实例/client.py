import time, struct
import socket

sk = socket.socket()

sk.connect(('127.0.0.1', 9000))
time.sleep(0.5)

num = struct.unpack('i', sk.recv(4))
print(sk.recv(num[0]).decode('utf-8'))
print(sk.recv(1024))
