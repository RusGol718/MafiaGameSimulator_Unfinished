from Classes.Class_Player import *
from Classes.Class_Role import *

class Day_Action:
  day_actions = []
    
  def __init__(self, name_of_action, action_function=None):
      self.name_of_action = name_of_action


  def do_action(self, action_function=None):
    self.action_function()


    
day_action = Day_Action("Voting")