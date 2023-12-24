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
    info()
        
elif Language == "2" or Language == "zh":
    lang = "zh"
    print("初始化完成")
    os.system("cls")
    info()
#启动
while True:
    #判断 
    path = os.getcwd()
    print("")
    link = input("MS" + " " + path + ">")
    if link == "hello_world":
        hello_world()
        continue
    elif link == "os":
        os_system()
        continue
    elif link == "cls":
        cls()
    elif link == "clear":
        clear()
    elif ".exe" in link or ".lnk" in link or ".txt" in link or ".zip" in link:
        os.system(link)
    elif link == "cpu_count":
        cpu_count()
        continue
    elif link == "list":
        list()
        continue
    elif link == "version":
        print("Moon command version 1.0.3")
        print("Moon commandbase version 0.1.1")
        continue
    elif link == "exit":
        print("bye")
        break
    elif link == "delete":
        delete()
        continue
    elif link == "rm":
        rm()
        continue
    elif link == "dir":
        dir()
        continue
    elif link == "cd":
        cd()
        continue
    elif link == "println":
        println()
        continue
    elif link == "echo":
        echo()
        continue
    elif link == "printf":
        printf()
        continue
    elif link == "varprint":
        varprint()
        continue
    elif link == "intprint":
        intprint()
        continue
    elif link == "floatprint":
        floatprint()
        continue
    elif link == "chdir":
        chdir()
        continue
    elif link == "copy":
        copy()
        continue
    elif link == "move":
        move()
        continue
    elif link == "rename":
        rename()
        continue
    elif link == "mkdir":
        mkdir()
        continue
    elif link == "md":
        md()
        continue

    elif link == "ls":
        ls()
        continue
    elif link == "var":
        var()
        continue
    elif link == "int":
        int()
        continue
    elif link == "float":
        float()
        continue
    else:
        if lang == "zh":
            print("'"+ link + "'"+" " + "不是内部或外部命令，也不是可运行的程序或批处理文件" + "\n")
        else:
            print("'"+ link + "'"+" " + "is not an internal or external command, nor a runnable program or batch file" + "\n")