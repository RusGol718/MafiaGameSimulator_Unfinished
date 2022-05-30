import json
from Utilities.F_setget_path import getpath2

def writing_json(data, filename, folder_name:str=None, subfolder_name:str=None):
  path = getpath2(filename, folder_name, subfolder_name)
  with open(path, "w+") as file:
    json.dump(data, file, indent=6)
  return data

def appending_json(data, filename, folder_name:str=None, subfolder_name:str=None):
  path = getpath2(filename, folder_name, subfolder_name)
  try:
    with open(path, "a+") as file:
      json.dump(data, file, indent=6)
    return data
  except:
    writing_json(data, filename, folder_name, subfolder_name)
