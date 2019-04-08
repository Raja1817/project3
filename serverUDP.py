import socket
import ujson

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("socket created")
port= 12000
s.bind(('',port) )
print("socket binded to 12000")
#s.listen()

while True:
    d, addr =s.recvfrom(1024)
    print("got connection from {}".format(addr))
    data =ujson.loads(d.decode('utf-8'))		
    print("received {}".format(data))
    msg = "string"
    s.sendto(ujson.dumps(msg).encode('utf-8'),addr)



