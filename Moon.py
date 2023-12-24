file = input("请输入你的文件:") #输入要运行的文件

def aout(a,b): ##定义aout模块，包括定义a,b
    return a + b ## 返回a+b
with open(file) as rf: 
    content = rf.read()
    if "main:" in content:
        content = content.replace("main:", "")
        if "aout" in content:
            content = content.replace("aout", "")
            result = eval(content)
            print(result, dict(aout=aout))
        else:
            print(content)
    else:
        print("error")
