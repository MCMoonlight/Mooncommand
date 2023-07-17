from logging import info
import os
import time


def list():
    list = os.listdir()
    list = str(list)
    print(list)


def cpu_count():
    cpu_count = os.cpu_count()
    cpu_count = int(cpu_count)
    time.sleep(5)
    print("————————————————————————————————")
    print("your CPU count is " + str(cpu_count))
    print("————————————————————————————————")


def hello_world():
    print("————————————————————————————————")
    print("hello world")
    print("hello I'm hacker.")
    print("I'm going to help you")
    print("awa")
    print("————————————————————————————————")


def os_system():
    time_cout = 0
    while time_cout <= 3:
        cmd = input("Please enter your command:")
        cmd = str(cmd)     
        os.system(cmd)
        time_cout += 1
        continue

def help():
    print("————————————————————————————————")
    print("help list:")
    print("1. list")
    print("2. cpu_count")
    print("3. hello_world")
    print("4. cmd_command")
    print("5. help")
    print("6. exit")
    print("7. ls")
    print("————————————————————————————————")


def ls():
    print("————————————————————————————————")
    list = os.listdir()
    list = str(list)
    print(list)
    print("————————————————————————————————")


def admin():
    info("admin")
    username = input("Enter admin username:")
    password = input("Enter admin password(int):")
    password = str(password)
    username = str(username)
    def admin_version():
        print("pythoncmd version 0.2 build10")
        print("pythoncmdlink version 0.12.4 build13")
        print("debugcmdlink version 0.3.3 build12")
    if username == "adminroot" and password == "adminroot114514":
        print("hi" + " " + username)
        while True:
            adminlink = input("adminlink command:")
            if adminlink == "admin_version":
                admin_version()
                continue
            if adminlink == "exit":
                info("bye admin command")
                break
            else:
                print("error: unknown command")

def delete():
    dellink = input("delete files:")
    os.remove(dellink)
