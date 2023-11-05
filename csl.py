#模块
from cslCommand import *
from CSLinitialize import *
import time
#初始化
initialize();
print("初始化完成")
os.system("cls")
print("csl command [version 1.0.1]")
print("MCMoonlight Team Corporation. 保留所有权利.")
print("\n")        
#启动
while True:
    #判断 
    link = input("command:")
    if link == "hello_world":
        hello_world()
        continue
    elif link == "cmd_command":
        os_system()
        continue
    elif link == "cpu_count":
        cpu_count()
        continue
    elif link == "list":
        list()
        continue
    elif link == "help":
        help()
        continue
    elif link == "version":
        print("csl command version 1.0.1")
        print("csl commandbase version 0.0.1")
        continue
    elif link == "exit":
        print("bye")
        break
    elif link == "delete":
        delete()
        continue
    elif link == "ls":
        ls()
        continue   
    else:
        print("error: unknown command")    