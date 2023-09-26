import socket

ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(('',7765))

ss.listen(100)

while True:
    c,addr = ss.accept()    
    print(f'connection from {addr}')
    print(c.recv(10240).decode())
    c.close()
    
