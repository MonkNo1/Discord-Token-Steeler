# this file is used to run the bat file and communicate throungh it 
import subprocess as sb 
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filepath= dir_path+"\steal.bat"


def runbat():
    p = sb.Popen(filepath, shell=False, stdout = sb.PIPE)
    stdout, stderr = p.communicate()

