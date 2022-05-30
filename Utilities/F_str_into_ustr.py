def turn_str_into_unicode_str(string):
  if type(string) is str:
    unicode_string = u"{}".format(string)
    return unicode_string

  elif (type(string) is int) or (type(string) is float) or (type(string) is bool):
    turn_str_into_unicode_str(str(string))
  else:
    return False
    # turns str, int, float and bools into a raw string
    #raw strings ignore 