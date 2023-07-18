from csllogin import *
from cslupdate import *
import wget

def initialize():
    url = "https://gitee.com/bilibiliFSRH/cslcommand/raw/main/version"
    wget.download(url)
    verfile = open("version", "r")
    try:
        version = verfile.read()
    finally:
        verfile.close()
    print(version)
    if version == "1.0.0":
        print("ok to run")
    else:
        cslupdate();
    
initialize()