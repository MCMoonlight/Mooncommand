from csllogin import *
from cslupdate import *

def initialize():
    verfile = open("version", "r")
    try:
        version = verfile.read()
    finally:
        verfile.close()
    if version == "1.0.0":
        print("ok to run")
    else:
        cslupdate();
    