def turn_str_into_raw_str(string):
  if type(string) is str:
    raw_string = r"{}".format(string)
    return raw_string

  elif (type(string) is int) or (type(string) is float) or (type(string) is bool):
    turn_str_into_raw_str(str(string))
  else:
    return False
# turns str, int, float and bools into a unicode string