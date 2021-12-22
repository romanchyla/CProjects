import os
from functools import wraps

import rutils


def inprojhome(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        config = rutils.load_config()
        curdir = os.getcwd()
        try:
            os.chdir(config["PROJ_HOME"])
            f(*args, **kwargs)
        finally:
            os.chdir(curdir)

    return wrapper
