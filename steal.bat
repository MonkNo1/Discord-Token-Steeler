@echo off 
cd /D %appdata%\discord
@REM dir
tar -cvzf locked.tar.gz GPUCache "Code Cache" Cache
ren locked.tar.gz locked
move locked E:\programing\sh\bash
@REM pause