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
    