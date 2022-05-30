from Classes.Class_Player import *
from Classes.Class_Role import *

class Night_Action:
    night_actions = []
    
    def __init__(self, name_of_action, do_action):
        self.name_of_action = name_of_action

	


class Sleep(Night_Action):

  def set_player_to_sleep(self):
    print("Sleeping")


    
      
sleep = Sleep("Sleep")
heal = Night_Action("heal")
search = Night_Action("search")
maf_kill = Night_Action("mafia kill")
assassin_kill = Night_Action("assassin_kill")