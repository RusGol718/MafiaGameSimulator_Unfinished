from Classes.Class_Role import *
from Utilities.F_print_plain_card import *
class RoleCard:

  def __init__(self, height, width, representing_role=None):
    self.h = height
    self.w = width
    self.representing_role = representing_role
    
    if self.representing_role is None:
      self.card = draw_plain_card(self.h, self.w)


