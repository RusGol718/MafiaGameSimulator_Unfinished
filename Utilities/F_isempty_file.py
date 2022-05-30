import os
from Utilities.F_str_into_rstr import turn_str_into_raw_str as rstr
from Utilities.F_exist_file import exist_file

def isempty_file(path:str):
    raw_path = rstr(path)
    if exist_file(raw_path):
        if os.stat(raw_path).st_size == 0:
            return True
        else:
            return False
# Checks if txt file is empty returns true, else returns false