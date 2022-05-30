from Utilities.F_setget_path import getpath2

def reading_multi_strings(filename, folder_name:str=None, subfolder_name:str=None):
  path = getpath2(filename, folder_name, subfolder_name)

  with open(path, "r") as file:
    data = file.readlines()
    
  return data

def reading_2D_lists(filename, folder_name:str=None, subfolder_name:str=None):
  path = getpath2(filename, folder_name, subfolder_name)

  with open(path, "r") as file:
    array2D = [line.split(",") for line in file]
    return array2D