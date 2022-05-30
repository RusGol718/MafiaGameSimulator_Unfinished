import os
from Utilities.F_str_into_rstr import turn_str_into_raw_str as rstr

def exist_file(path):
    raw_path = rstr(path)
    if os.path.isfile(raw_path):
        return True
    else:
        return False

#Checks and returns true, if file exist, else returns false