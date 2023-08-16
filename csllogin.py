#模块
import os
import wget

def login():
    url2 = "https://gitee.com/bilibiliFSRH/cslcommand/raw/main/cslusername.py"
    url1 = "https://gitee.com/bilibiliFSRH/cslcommand/raw/main/csluserpass.py"
    wget.download(url2)
    wget.download(url1)
    userfile = open("cslusername.txt", "r")
    try:
        username = userfile.read()
    finally:
        userfile.close()
    userfile = open("csluserpass.txt", "r")
    try:
        password = userfile.read()
    finally:
        userfile.close()
    password = str(password)
    username = str(username)
    password1 = input("Enter csl account password(no csl account please enter NO)")
    username1 = input("Enter csl account username(no csl account please enter NO)")
    if password1 == password or username1 == username:
        print("Welcome csl users")
    else:
        print("OK")
    os.system("del cslusername.txt")
    os.system("del cslpassword.txt")