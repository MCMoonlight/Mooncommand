#模块
def login():
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
        print("OK")
    else:
        print("Welcome csl users")