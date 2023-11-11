#模块
from cslCommand import *
#初始化
print("please set your Language:")
print("1.en")
print("2.zh")
Language = input()
if Language == "1" or Language == "en":
    lang = "en"
    print("Initialization complete")
    os.system("cls")
    print("Moon command [version 1.0.2]")
    print("MCMoonlight Team Corporation.")
        
elif Language == "2" or Language == "zh":
    lang = "zh"
    print("初始化完成")
    os.system("cls")
    print("Moon command [version 1.0.2]")
    print("MCMoonlight Team Corporation.")    
#启动
while True:
    #判断 
    path = os.getcwd()
    link = input("PS" + " " + path + ">")
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
        print("Moon command version 1.0.2")
        print("Moon commandbase version 0.0.1")
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
        if lang == "zh":
            print("'"+ link + "'"+" " + "不是内部或外部命令，也不是可运行的程序或批处理文件" + "\n")
        else:
            print("'"+ link + "'"+" " + "is not an internal or external command, nor a runnable program or batch file" + "\n")