import os
import sys
#import numpy
#import panda
#import math
import json
from functools import reduce

from Utilities.Class_Stack import Stack
from Utilities.F_reading_2D_lists import reading_multi_strings as r_multystr
from Utilities.F_reading_json import reading_json as rjson
from Utilities.F_writing_json import writing_json as wjson

from Classes.Class_Player import *
from Classes.Class_Role import *
from Classes.Class_Map import *
from Classes.Class_Location import *
from Classes.Class_RoleCard import *
from Classes.Actions.Class_NightAction import *
from Classes.Actions.Class_DayAction import *
from Classes.Class_Game import *
clear = lambda: os.system('cls')
#[print(map1.grid_map[:][row]) for row in range(3)]
#for i in range(7):
#  print(r_multystr("sun.txt","Files", "Pictures/Phases")[i])
games = [Game("", [3, 1, 1, 1, 1]) for i in range(1)]
#[print(game.hash) for game in games]
map1.set_locations(len(Player.players))
#map1.setup_map()
#print(map1.setup_map())
#[(i.role.possible_nightactions[0].set_player_to_sleep()) for i in Player.players]
#print(rjson("first_names2.json", "Files", "Loading"))
card1 = RoleCard(8,12)
[Game.run() for game in games]
#[print(i.nick, i.role.name, i.is_human) for i in Player.players]
