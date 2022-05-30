from Classes.Actions.Class_NightAction import *
from Classes.Actions.Class_DayAction import *
from Classes.Class_RoleCard import *
from Classes.Class_Player import *

class Role:
  roles = []
  def __init__(self, name:str, possible_nightactions:list, possible_dayactions:list, card=None, discription=None):
    #contructor
    self.name = name
    if possible_nightactions is None:
      raise Exception("Need a night action") #Raises an error if night action list not given
    else:
      self.possible_nightactions = possible_nightactions
    if possible_dayactions is None:
      raise Exception("Need a day action") #Raises an error if day action list not given
    else:
      self.possible_dayactions = possible_dayactions
    self.card = card

    self.discription = "discription"
    Role.roles.append(self)

  def available_actions(self):
    if self.name.upper() == "CITIZEN":
      return ['sleep']
    elif self.name.upper() == "DOCTOR":
      each_player.role.possible_nightactions.append(sleep)
      each_player.role.possible_nightactions.append(heal)
    elif each_player.role.name.upper() == "SHERIFF":
      each_player.role.possible_nightactions.append(sleep)
      each_player.role.possible_nightactions.append(search)
    elif each_player.role.name.upper() == "MAFIA":
      each_player.role.possible_nightactions.append(sleep)
      each_player.role.possible_nightactions.append(maf_kill)
    elif each_player.role.name.upper() == "ASSASSIN":
      each_player.role.possible_nightactions.append(sleep)
      each_player.role.possible_nightactions.append(assassin_kill)


    

  @staticmethod
  def set_nightaction_list(pls:list):
    for each_player in pls:
      if each_player.role.name.upper() == "CITIZEN":
        each_player.role.possible_nightactions.append(sleep)
      elif each_player.role.name.upper() == "DOCTOR":
        each_player.role.possible_nightactions.append(sleep)
        each_player.role.possible_nightactions.append(heal)
      elif each_player.role.name.upper() == "SHERIFF":
        each_player.role.possible_nightactions.append(sleep)
        each_player.role.possible_nightactions.append(search)
      elif each_player.role.name.upper() == "MAFIA":
        each_player.role.possible_nightactions.append(sleep)
        each_player.role.possible_nightactions.append(maf_kill)
      elif each_player.role.name.upper() == "ASSASSIN":
        each_player.role.possible_nightactions.append(sleep)
        each_player.role.possible_nightactions.append(assassin_kill)
      else:
        return False

      return (each_player.role.possible_nightactions)
  @staticmethod
  def set_dayaction_list(pls:list):
    for each_player in pls:
      each_player.role.possible_dayactions.append()


    


citizen = Role("CITIZEN", [sleep], [day_action], discription="The civilian is the most common role in the game, and the easiest to play. The main task of the citizens is to execute all mafiosi and save the city. At night, civilians sleep, and in the morning they vote against the players who are suspected of involvement in the mafia clan (or assassin). Who will be executed is decided by the majority of votes, so it is very important to cast your vote against the real mafia. If, during the day, votes are equal, revoting will take place.\n Citizents win if they get rid of mafia or assassin.")

doctor = Role("DOCTOR", [sleep, heal], [day_action], discription="The doctor can visit one player every night and save his life in case of an attempt to kill him by a mafia or a maniac. The doctor, like all active roles, cannot heal at night to himself.")

sheriff = Role("SHERIFF", [sleep, search], [day_action], discription="The sheriff visits one of the players every night, determining what role the suspect plays in the party. His task is to figure out all the representatives of the mafia clan as quickly as possible and, with the support of civilians, put them to death. He wins with civilians")
mafia = Role("MAFIA", [sleep, maf_kill], [day_action], discription="The role of the mafia represents the dark side of the game confrontation. There are several players in each game with this role. The mafia, in order to win, will have to gradually kill most of the civilians every night in order to capture the city (1:1 ratio. Do not forget that the mafia should be wary of the sheriff, who can find out their role, and the assassin, who also can accedently kill them.")
assassin = Role("ASSASSIN", [sleep, assassin_kill], [day_action], discription="Assassin is one of the most controversial roles in the game. Despite a bad reputation among the citizens of the city, a assassin can help civilians by killing mafia members at night. However, both ordinary citizens and the sheriff or a doctor can suffer from his actions.\n The assassin can win only if the mafia in the city is completely destroyed and he is in a 1:1 ratio with any civilians, sheriffs or doctors.")
