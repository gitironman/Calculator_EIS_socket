import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1', 9000))

cache_dic = {}  # {1:{'发送者':[msg1,msg2],'发送者2':[msg1,msg2]}}
addr_dic = {}
while True:
    operate, addr = sk.recvfrom(1024)
    # online
    # 把qq号码和addr存到addr_dic
    # offline
    # 把qq号码和addr从addr_dic中删掉
    # send
    # 将信息存储在cache_dic
    # recv(手动或者自动)
    # 检查cache_dic有没有属于你的消息
    # 如果有,有几条,client端应该根据信息的条数进行对应的接收

# qq 微信 udp协议在推送消息
# tcp 可靠的
# udp 不可靠
# 可靠传输的? 使用udp协议实现的回执
