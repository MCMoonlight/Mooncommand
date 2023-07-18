#模块
from cslCommand import *
from CSLinitialize import *
#启动
while True:
    #判断 
    link = input("link command:")
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
        print("csl command version 1.0.0")
        print("csl commandbase version 0.0.1")
        continue
    elif link == "ver":
        print("pythoncmd version 1.0.0")
        print("pythoncmdlink version 0.0.1")
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
    elif link == "admin":
        admin()
        continue
    else:
        print("error: unknown command")    