import json
import csv
from Utilities.F_setget_path import getpath2

def reading_json(filename, folder_name:str=None, subfolder_name:str=None):
  path = getpath2(filename, folder_name, subfolder_name)

  with open(path, "r") as file:
    data = json.load(file)
    
  return data

def reading_csv(filename, folder_name:str=None, subfolder_name:str=None):
  path = getpath2(filename, folder_name, subfolder_name)

  with open(path, "r") as file:
    data = csv.reader(file)
    
  return data