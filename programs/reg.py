import time

f = open("name.sys", "w")
x = input("enter_your_name ")
f = open("name.sys", "a")
f.write(x)
f.close()
time.sleep (2.5)
p = open("pass.sys", "w")
y = input("create password: ")
a = input("enter your password again: ")
p = open("pass.sys", "a")
p.write(y)
p.close()
print("Thank you for registering LopaOS")
time.sleep (1)
print("Now you no longer have to open reg.bat but just open os.bat")
time.sleep(5)
quit()