import json
import socket

sk = socket.socket(type = socket.SOCK_DGRAM)
addr = ('127.0.0.1',9000)
# 发送上线通知
info = {'operate':'online','qq':1}
json_info = json.dumps(info)
sk.sendto(json_info.encode('utf-8'),addr)  # 上线之后通知server

# 给好友发送消息
info = {'operate':'send_msg','to_qq':2,'msg':'你好'}
json_info = json.dumps(info)
sk.sendto(json_info.encode('utf-8'),addr)