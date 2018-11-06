import socket
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',5003))
a=s.recv(1024)
print('-->'+a.decode('utf-8'))
s.send(b'hello server,I am a client')
time.sleep(1)
s.send(b'please let me know when you receive it')
time.sleep(5)
print('-->'+s.recv(1024).decode('utf-8'))
s.close()