import json
import socket

sk = socket.socket(type = socket.SOCK_DGRAM)
addr = ('127.0.0.1',9000)
sk.bind(addr)
dic = {}       # {qq:addr}
cache_dic = {} # {to_qq : [msg,msg1]}
while True:
    content,addr = sk.recvfrom(1024)
    msg = content.decode('utf-8')
    msg_dic = json.loads(msg)
    if msg_dic['operate'] == 'online':
        qq = msg_dic['qq']
        dic[qq] = addr   # 记录了client端的qq号码和端口号
        if qq in cache_dic:
            for msg in cache_dic[qq]:
                sk.sendto(msg, addr)
    elif msg_dic['operate'] == 'send_msg':
        to_qq = msg_dic['to_qq']
        if dic.get(to_qq) :
            sk.sendto(msg_dic['msg'].encode('utf-8'),dic[to_qq])
        elif to_qq in cache_dic:
            cache_dic[to_qq].append(msg_dic['msg'].encode('utf-8'))
        else:
            cache_dic[to_qq] = [msg_dic['msg'].encode('utf-8')]
