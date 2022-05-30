from Utilities.F_str_into_rstr import turn_str_into_raw_str as rstr
from Files.File_Paths.Const_paths import base


def getpath(file:str, folder:str=None, subfolder:str=None):
  if (folder is None) and (subfolder is None):
    path = rstr(base + "/" + file)
    #file is file + "." + extention (txt, json)
    return path # No folder or subfolder is given, so the file path is base in replit
  
  if (folder is not None) and (subfolder is None):
    path = rstr(base + "/" + folder + "/" + file)
    return path  #No subfolder is given, so file is saved in the folder given

  if (folder is not None) and (subfolder is not None):
    path = rstr(base + "/" + folder + "/" +  subfolder + "/" + file)
    return path #File is saved into a subfolder

def getpath2(file:str, folder:str=None, subfolder:str=None):
  if (folder is None) and (subfolder is None):
    path = rstr(file)
    return path

  if (folder is not None) and (subfolder is None):
    path = rstr(folder + "/" + file)
    return path
  
  if (folder is not None) and (subfolder is not None):
    path = rstr(folder + "/" +  subfolder + "/" + file)
    return path 
  #getpath2 function does the same but without a full dir path as full path is not needed in replit. On a PC a full path is needed though.