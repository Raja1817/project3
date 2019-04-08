import socket
import ujson

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port= 12000

#s.connect( ('192.168.1.220' , port) )
print("connecting to {}:{}".format('192.168.1.220' , port))
s.sendto(ujson.dumps('12').encode('utf-8'), ('192.168.1.220' , port) )
msg, addr =s.recvfrom(1024)
d = ujson.loads(msg.decode('utf-8'))  
print("received {} ".format(d))
s.close()
