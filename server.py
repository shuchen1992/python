import socket
import time

host = '192.168.1.106'
post =25363
BUFSIZE = 1024
tcpsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr =(host,post)
tcpsocket.bind(addr)
tcpsocket.listen(5)



while True:
    clisocket,addr = tcpsocket.accept()
    while True:
        data,chost = clisocket.recvfrom(BUFSIZE)
        if not data:
            break
        else:
            clisocket.send("the %s time is %s"%(data,time.ctime()))
