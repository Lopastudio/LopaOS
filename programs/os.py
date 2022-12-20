import os
import subprocess
import time
import os.path
import library
from os import path

ver = 1.4

#Load Print
print ("Loading Files necessary to boot LopaOS")
time.sleep(0.3)
print ("Password File:"+str(path.exists('pass.sys')))
time.sleep(0.3)
print ("User Information File:" + str(path.exists('name.sys')))
time.sleep(0.3)
"""
print ("deldata:" + str(path.exists('deldata.bat')))
time.sleep(random.randint(1,2))
print ("edit:" + str(path.exists('edit.py')))
time.sleep(random.randint(1,2))
print ("filebrowser:" + str(path.exists('filebrowser.py')))
time.sleep(random.randint(1,2))
print ("get-pip" + str(path.exists('get-pip.py')))
time.sleep(random.randint(1,2))
print ("reg" + str(path.exists('reg.py')))
time.sleep(random.randint(1,2))
print ("start_sound:" + str(path.exists("start.wav")))
time.sleep(random.randint(1,2))
print ("logo:" + str(path.exists("logo.ico")))
time.sleep(random.randint(1,2))
"""

print ("If one of the file didn´t exist")
print ("Run:  On Windows: ´reg.bat´  Or on Linux And MacOS Run: ´reg.py´ in directory ´programs´")


f = open("name.sys", "r")
p = open("pass.sys", "r") 
  

#Infinity Command Calling loop
while (True):
  
    i = input("\\Main\ ")
    if i == "help":
        library.help()
    elif i == "stop":
        print("Good bye " + x)
        time.sleep(3)
        quit()

    elif i == "notepad":
        os.system('python3 edit.py')
    elif i == "exit":
        print("Good bye " + x)
        time.sleep(3)
        quit()
    elif i == 6:
        fileo = input("enter name of file")
        fileop = fileo + ".py"
        print (fileop)
        os.system('python ' + fileop)
    elif i == "open":
        fileo = input("enter name of file")
        fileop = fileo + ".py"
        print (fileop)
        os.system('python ' + fileop)
    elif i == "calc":
        library.calc()
    elif i == "dir":

        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            print (f)
    elif i == "files":
        os.system('python filebrowser.py')
        
    elif i == "ver":
        print ("LopaOS - " + ver)
        print ("Library version - " + libver)
    else:
        print("Failed to execute the instruction. Instruction that you provided is invalid or is not correctly formated.")
