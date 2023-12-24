file = input("请输入你的文件:")

def aout(a,b):
    return a + b
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
