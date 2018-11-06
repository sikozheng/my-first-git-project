import socket
import threading
import time
def dealclient(sock,add):
    print('accept new connection from %s:%s'% add)
    sock.send(b'hello,I am a server')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        print('-->%s'%data.decode('utf-8'))
        time.sleep(3)
        # sock.send(b'hello,i am a client,your msg have been received')
        sock.send(b'loopmsg: %s'  % data.decode('utf-8').encode('utf-8'))
    sock.close()
    print('connection from %s%s closed'%add)

if __name__=="__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',5003))
    s.listen(5)
    print('waiting for connection..')
    while True:
        sock,add=s.accept()
        t=threading.Thread(target=dealclient,args=(sock,add))
        t.start()