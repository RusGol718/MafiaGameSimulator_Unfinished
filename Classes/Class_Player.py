import json
from random import randint as rint
from random import choice
from Utilities.F_reading_json import reading_json as rjson
from Utilities.F_writing_json import writing_json as wjson
from Utilities.F_writing_json import appending_json as ajson

from Utilities.Class_Stack import Stack
from main import map1
#from Classes.Class_Game import Game.map
from Classes.Class_Role import *
from Classes.Class_Map import *
from Classes.Class_Location import *
from Classes.Class_Enum_Colour import Colour

class Player:
  #The following are class variables that are not instant variables
	players = []
	alive_ingame_pl = []
	pl_attr = []
	number_pl = 0
	mafia = []

	def __init__(self, nickname, role, colour=None, loc=None, points_l=None, games_pll=None, is_human=None, is_alive=None, is_asleep=None, is_lying=None, is_healed=None, you_voted_pl=None, voted_for_you=None, assasin_aim=None, mafia_aim=None, sus_roles=None):
    #Constructor
		
		if nickname in ["", " ", "  ", "\n", "\t", "\a"]:
			try: #This is a try/except statement that will load random names from A Json file 
				names = rjson("first_names2.json", "Files", "Loading")
        #Rjson is a function that will read json files from a parameterised file path 
        #The except statement below will set names list if the Json file is not loaded properly
			except FileNotFoundError:
				names = ["Maha", "Reem", "Farida", "Aya", "Nada", "Rita", "Arthur",	"Joao", "Pedro",	"Heitor",	"João", "Lucas",	"Davis", "Luke",	"Davi", "Lucca", "David", "Charlotte", "Amy", "Olivia", "Elizabeth", "Alex", "Mark", "Tom", "Chris", "Victoria", "Ada", "Leon", "Paula", "Karl", "Ruslan", "James", "Naomi", "Eve", "Theodore", "Theo", "Timothy", "Christy", "Christina", "Penny", "Curtis", "Ian", "Carl", "Andrea", "Philip", "Sofia", "Sophia", "Troy", "Isabel", "Oyun", "Ulzi", "Alexey", "Iona", "Claire", "Hannah", "Harry", "Phil", "Fiona", "Leia", "Barry", "Adam", "Arthur", "Sam", "Samantha", "April", "Summer", "June", "Hope", "Faith", "Jack", "Jason", "Heidi", "Pat", "Rochel", "Michelle", "Tina", "Ellis", "Nick", "Michael", "Thomas", "Bernadette", "Wilson", "Sherlock", "Fran", "Gary", "Ebi", "Kristine", "Kristina", "Irina", "Alina", "Vicky", "Bill", "Bob", "Dennis", "Jasper", "Rose", "Sapphire", "Ruby", "Paul", "Alexa", "Elisha", "Howard", "Mathew", "Matt", "Matteo", "Romeo", "Juliet", "Olivia", "Mia", "Camilia", "Amanda", "Avva", "Ali", "Kai", "Feng", "AbulFazl", "Lei", "Chiahao", "Chiang", "Rustan", "Ruslana", "Marx", "Lenin", "Stalin", "Leonardo", "Gradsciy", "Il'ya", "Aurora", "Peter", "Ivan", "Nicholai", "Edgenii", "Nasya", "Nastya", "Anastasia", "Anastas'", "Zoe", "Boris", "Rus", "Comrade", "T-800", "Terminator", "Ruskaya", "Paren'", "Joe", "Abbie", "Demos", "Fobos", "Henry", "William", "Will", "Tanyam", "Kelimin", "Ryski", "Alviera", "Adew", "Mahatdir", "Alfazri", "Aryantie", "Cemeng", "Norzuhana", "Adzmel", "Rhafi", "Ariel"]

			if choice(names) not in [i.nick for i in Player.players]:
				self.nick = choice(names)
			else:
				self.nick = choice(names) + str(rint(100, 999))
				wjson("first_names2.json", r"U:", "Documents")
	#This "If" statement will check if there are duplicate names and if there is any the names will receive a random integer from 100-999 at the end of the name 
		else:
			self.nick = nickname # sets the nickname 

    #These "if" statements will set colours according to their roles. For example, the doctor will receive a red colour.    
		self.role = role
		if colour is None:
			if self.role == citizen:
				self.colour = Colour.RED
			elif self.role == doctor:
				self.colour = Colour.RED
			elif self.role == sheriff:
				self.colour = Colour.RED
			elif self.role == assassin:
				self.colour = Colour.BLUE
			elif self.role == mafia:
				self.colour = Colour.BLACK
			else:
				self.colour = Colour.NO_COLOUR
    # Sets up the Enum colours from the Enum class.
		else:
			self.color = colour #The user doesn't need to choose a colour but can.

		if loc is None:
			self.loc = loc_pl
		else:
			self.loc = loc
    
    #The points are automatically set to 0
		if points_l is None:
			self.points_l = 0
		else:
			self.points_l = points_l
    #This automatically sets the amount of games played to 0 as well as wins, losses and draws. 
		if games_pll is None:
			self.games = [0, 0, 0]
		else:
			self.games = games_pll
    #Automatically sets all players to bots.
		if is_human is None:
			self.is_human = False
		else:
			self.is_human = is_human
		#Automatically set everyone in the game from the beginning to alive. 
		if is_alive is None:
			self.is_alive = True
		else:
			self.is_alive = is_alive
    #Automatically set all players to sleeping mode.
		if is_asleep is None:
			self.is_asleep = True
		else:
			self.is_asleep = is_asleep
    #Set all players as not lying.
		if is_lying is None:
			self.is_lying = False
		else:
			self.is_lying = is_lying
    #Set every player to not healed. When a player is visited by a doctor this will be set to true. 
		if is_healed is None:
			self.is_healed = False
		else:
			self.is_healed = is_healed
    #This is a stack of players that you have voted for. 
		if you_voted_pl is None:
			self.you_voted = Stack(10^6)
		else:
			self.you_voted = you_voted_pl
    #This is a stack of players that voted against you. 
		if voted_for_you is None:
			self.voted_for_you = Stack(10^6)
		else:
			self.voted_for_you = voted_for_you
    #A json file that will write/read players that have been suspected e.g. players that have voted agaisnt you. 
		if sus_roles is None:
			with open("Files/Loading/sus_roles.json", "r") as file:
				data = json.load(file)
			self.sus_roles = data
    
		Player.players.append(self)  # adds it to the players list
#    if self.is_alive:
#      Player.players.append(self)
		Player.number_pl += 1 #increases the number of players by 1 when a new one is created
		if self.is_alive:
			Player.alive_ingame_pl.append(self)
    #Sets the list of all Mafia players 
		if self.role is mafia:
			Player.mafia.append(self)
  
	def vote(self, other_player=None):
    #A method that allows the voting to take place. 
		if self.is_human:
			not_entered = True
			#Checks if the player is human. 
			while not_entered:
				vote = input("\nPlease enter the nickname of the player you think is Mafia or Assassin\n")
				print()
				if vote in [i.nick for i in Player.alive_ingame_pl] and vote != self.nick:
          #Can't vote for self
					not_entered = False
					other_player = [i for i in Player.alive_ingame_pl if i.nick == vote][0]
					self.you_voted.Push(other_player)
					other_player.voted_for_you.Push(self)
          # human voting for some player
				else:
					print(f"Your vote --> {vote}.\nYou can't vote for your self nor can you vote for dead or non-existant players")
					print("Please retry" + "."*rint(3, 10))
		else:
			self.you_voted.Push(other_player)
			other_player.voted_for_you.Push(self)
			self.sus_roles.append(other_player)
      #bot vote
		print(f"{self.nick} has voted for {other_player.nick}")
    #says who voted for who



	@staticmethod
	def voting_intellegent():
    #lets people randomly vote i.e. for bots. 
		if players is None:
			for i in Player.alive_ingame_pl:
				if i.is_human:
					i.vote()
          #Allow players to choose who they vote for. 
				else:
					i.vote(i.vote_say(map1))
					#Calculates which player when against the bot and votes for it
          # vote by calling the method
		else:
			[i.vote() for i in players if i.alive_ingame_pl]
			[i.vote_say(map1) for i in players if not i.is_human]

	@staticmethod
	def revoting_intellegent(revote_pls:list):
		if len(revote_pls) > 1:
			Player.voting_intellegent(revote_pls)
			new_revote_pls = Player.execution()
			revote_pls = new_revote_pls

	def execute(self):
		print(f"{self.nick}: These are my last words")
		self.is_alive = False
		Player.alive_ingame_pl.remove(self)
    #execution of indiviual player 
    
	@staticmethod
	def execution():
    #a method that creates random voting with random execution 
		votes_dict = {i.nick:len(i.voted_for_you.items) for i in Player.players}
    # creating a dict of {Player:num of votes}
		max_vote = max(list(votes_dict.values()))

		for k in list(votes_dict):#itterate through keys of a dictionry 
				if votes_dict[k] < max_vote:
					votes_dict.pop(k, "No such player")#if the players not found it will print "no such player" 
				#filtering the dict to max votes per player
		pl_with_max_votes = []
		pl_nicks_with_max_votes = list(votes_dict.keys())#a list of dictionary keys 
		
		for i in range(len(pl_nicks_with_max_votes)):
			for j in range(len(Player.alive_ingame_pl)):
				if pl_nicks_with_max_votes[i] == Player.alive_ingame_pl[j].nick:
					pl_with_max_votes.append(Player.alive_ingame_pl[j])

		for i in Player.alive_ingame_pl:
			constant = "Player"
			print(f"{constant:>40} {i.nick} recieved {len(i.voted_for_you.items)} number of votes")

		if not len(pl_with_max_votes) == 1:
			Player.revoting_intellegent(pl_with_max_votes)
		else:
			Player.execute(pl_with_max_votes[0])
		
		return pl_with_max_votes


	def assssin_kill_bot_intellegent(self):
		if self.role == assassin: #Only an assassin can do this action.
			aimed_pl = self.sus_roles.Pop()
			# randomly select a player target
			print("Assassin has chosen a soul to torture...")
			aimed_pl.assassin_aim = True
			# Preform the action
			return aimed_pl

	def assassin_human_kill(self):
		if self.role == assassin and self.is_human == True:
			not_entered = True
			#Checks if the player is human. 
			aimed_pl = input("\nPlease enter the nickname of the player you want to take revenge upon\n")
			if aimed_pl in [i.nick for i in Player.alive_ingame_pl] and self != self.nick: # validation
				#Can't assassinate your self or not alive players for self
				not_entered = False
			else:
				print("Sorry, can not preform action as you can not assassinate yourself or already dead players. Please try again...\n")
			aimed_pl.assassin_aim = True
			return aimed_pl

	@staticmethod
	def assassin_kill():
		human_targets = [pl.assssin_human_kill(pl) for pl in Player.alive_ingame_pl if pl.is_human == True]
		bot_targets = [pl.assssin_kill_bot_intellegent() for pl in Player.alive_ingame_pl if pl.is_human == False]
		aimed_pls = human_targets + bot_targets
		for pl in aimed_pls:
				if pl.is_healed:
					print("The doctor saved an individual from certain death...")
				else:
					pl.is_alive = False
					Player.alive_ingame_pl.remove(self)

	@staticmethod
	def move_random_on_map(map):
		offset = rint(1, len(Player.players))
		counter = 0
		for i in range(len(map.grid_map)):
			for j in range(len(map.grid_map[i])):
				if (counter != offset) and (map.grid_map[i][j] == loc_pl):
					counter +=1
				elif (counter == offset) and (map.grid_map[i][j] == loc_pl):
					coodinate = (i, j) #Find the 'X' player's coodinate

		direction = rint(0, 3)
		if direction == 0: # Move left
			try:
				next_coordinate = (coodinate[0]-1, coodinate[1])
			except IndexError:
				next_coordinate = (coodinate[0]+1, coodinate[1]) # bounce right
			finally:
				map.grid_map[coodinate[0]][coodinate[1]], map.grid_map[next_coordinate[0]][next_coordinate[1]] = map.grid_map[next_coordinate[0]][next_coordinate[1]], map.grid_map[coodinate[0]][coodinate[1]] #Swapping the values at those coodinates
		elif direction == 1: #Move up
			try:
				next_coordinate = (coodinate[0], coodinate[1]-1)
			except IndexError:
				next_coordinate = (coodinate[0], coodinate[1]+1) #bounce down
			finally:
				map.grid_map[coodinate[0]][coodinate[1]], map.grid_map[next_coordinate[0]][next_coordinate[1]] = map.grid_map[next_coordinate[0]][next_coordinate[1]], map.grid_map[coodinate[0]][coodinate[1]] #Swapping the values at those coodinates
		elif direction == 2: #move right
			try:
				next_coordinate = (coodinate[0]+1, coodinate[1])
			except IndexError:
				next_coordinate = (coodinate[0]-1, coodinate[1]) #bounce left
			finally:
				map.grid_map[coodinate[0]][coodinate[1]], map.grid_map[next_coordinate[0]][next_coordinate[1]] = map.grid_map[next_coordinate[0]][next_coordinate[1]], map.grid_map[coodinate[0]][coodinate[1]] #Swapping the values at those coodinates
		elif direction == 3: #Move down
			try:
				next_coordinate = (coodinate[0], coodinate[1]+1)
			except IndexError:
				next_coordinate = (coodinate[0], coodinate[1]-1) #bounce up
			finally:
				map.grid_map[coodinate[0]][coodinate[1]], map.grid_map[next_coordinate[0]][next_coordinate[1]] = map.grid_map[next_coordinate[0]][next_coordinate[1]], map.grid_map[coodinate[0]][coodinate[1]] #Swapping the values at those coodinates
				
	@staticmethod		
	def mafia_kill(self):
		mafia = [pl for pl in Player.alive_ingame_pl if pl.role == mafia]
		maf_aim = []
		for maf in mafia:
			if maf.is_human == True: # Human enteres who they want to kill
				not_entered = True
				while not_entered: # validation
					vote = input("\nPlease enter the nickname of the player you want get rid of for ever...\n")
					print()
					if vote in [i.nick for i in Player.alive_ingame_pl] and (vote not in [i.nick for i in mafia]):
						not_entered = False
						vote_pl  = [i for i in Player.alive_ingame_pl if vote == i.nick]
						maf_aim.append(vote_pl)
					else:
						print("Sorry, can not preform action as you can not get rid yourself, your team mafiosos or dead players. Please try again...\n")
			else:
				vote_bot = choice([pl for pl in Player.alive_ingame_pl if pl not in Player.mafia])
				maf_aim.append(vote_bot)
			maf_vote = max(set(maf_aim), key = maf_aim.count) #maximum votes recieved by mafia members(creates a freq table and takes the ,maximum)
			maf_vote.mafia_aim = True
			if maf_vote.is_healed: #Checks if the player was healed
				print("The doctor saved an individual from certain death...")
			else:
				pl.is_alive = False
				Player.alive_ingame_pl.remove(self)

	@staticmethod
	def sheriff_search():
		sheriff = [pl for pl in Player.alive_ingame_pl if pl.role == sheriff]
		if sheriff.is_human:
			not_entered = True
			while not_entered: # validation
				search_aim = input("\nPlease enter the nickname of the player you want invesigate\n")
				print()
				if search_aim in [i.nick for i in Player.alive_ingame_pl] and search_aim != sheriff.nick:
					not_entered = False
					search_aim  = [i for i in Player.alive_ingame_pl if search_aim == i.nick]
				else:
					print("Sorry, can not preform action as you can not investigate yourself, or dead people Please try again...")
		else:
			search_aim = choice([pl for pl in Player.alive_ingame_pl if pl.role != sheriff])

		print(f"\nThe player {search_aim.nick} is a\t\t {search_aim.role.name}")
		if search_aim.role == assassin or search_aim.role == mafia:
			sheriff.sus_roles.Push(search_aim) 

	@staticmethod
	def doctor_visit():
		doctor = [pl for pl in Player.alive_ingame_pl if pl.role == doctor]
		if doctor.is_human:
			not_entered = True
			while not_entered: # validation
				heal_aim = input("\nPlease enter the nickname of the player you want to heal\n")
				print()
				if heal_aim in [i.nick for i in Player.alive_ingame_pl] and heal_aim != doctor.nick:
					not_entered = False
					search_aim  = [i for i in Player.alive_ingame_pl if heal_aim == i.nick]
				else:
					print("Sorry, can not preform action as you're not god to heal yourself and you're not proficent enought to revive the dead. Please try again...")
		else:
			heal_aim = choice([pl for pl in Player.alive_ingame_pl if pl.role != doctor])
		heal_aim.is_healed = True

	def vote_say(self, map):
		offset = rint(1, len(Player.players))
		people_next2me = []
		locations_next2me = []
		counter = 0
		for i in range(len(map.grid_map)):
			for j in range(len(map.grid_map[i])):
				if (counter != offset) and (map.grid_map[i][j] == loc_pl):
					counter +=1
				elif (counter == offset) and (map.grid_map[i][j] == loc_pl):
					coodinate = (i, j) #Find the 'X' player's coodinate
		for i in range(coodinate[0]-1, coodinate[0]+2):
			if i < 0: #validating indexes x
				i=1
			elif i >= len(map):
				i = len(map) - 1
			for j in range(coodinate[1]-1, coodinate[1]+2):
				if i < 0: #validating indexes y
					i=0
				elif i >= len(map):
					i = len(map.traspose()) - 1

				if map.grid_map[i][j] == loc_pl:
					people_next2me.append(self.sus_roles.Pop())
				else:
					locations_next2me.append(map.grid_map[i][j])
		loc = choice(locations_next2me) # getting the closest location to yourself and another player by kings move (from chess)
		people_next2me = [i for i in people_next2me if i in Player.alive_ingame_pl]
		sus_pl = people_next2me[rint(0, len(people_next2me)-1)]
		if people_next2me != []:
			another_sus_pl = people_next2me[0]
			print(f" I saw player {sus_pl.nick} with {another_sus_pl.nick} at the {loc.name}")
			self.sus_roles.Push(another_sus_pl)
			self.sus_roles.Push(sus_pl)
			return sus_pl
		else:
			print(f" I saw player {sus_pl.nick} at the {loc.name}")
			self.sus_roles.Push(sus_pl)
			return sus_pl
		#choosing player that they suspects based on location, past behavior This is the most complicated algorithim
		
			