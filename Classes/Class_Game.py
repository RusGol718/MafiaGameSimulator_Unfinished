from functools import reduce
from random import shuffle
from random import randint
from operator import ixor as xor

from Utilities.F_reading_json import reading_json as rjson
from Utilities.F_writing_json import writing_json as wjson
from Utilities.F_reading_2D_lists import reading_2D_lists as r2Dtxt

#import Classes.Class_Player as Player
from Classes.Class_Player import *
from Classes.Class_Role import *
from Classes.Actions.Class_NightAction import *




#made needs to loaded to here

class Game:
	game_running = True # while game_running is main lopp
	number_nights_and_days_tuple = (0, 0) # 1st num are nights, 2nd are days
	hash_used = []
	players = []
	alive_players = []
	def __init__(self, title, roles_in_game:list, hash_id_game=None, mode="Classical", map=None):
    #constructor 
    
		if title == "":#default title of game is "Mafia Game"
			self.title = "Mafia Game" # setting up title of game
		else:
			self.title = title
    
		if type(roles_in_game) is list:
			if roles_in_game==[]:
        #paramitised file paths loading role data 
				roles_data = rjson("game_roles_setup.json", "Files", "Loading")
				self.roles_in_game = [i for i in roles_data if i >= 0] 
			
			else:
				self.roles_in_game = roles_in_game
      #dynamically generated players with all the roles 
			[Player("", citizen) for i in range(self.roles_in_game[0])]
			[Player("", doctor) for i in range(self.roles_in_game[1])]
			[Player("", sheriff) for i in range(self.roles_in_game[2])]
			[Player("", assassin) for i in range(self.roles_in_game[3])]
			[Player("", mafia) for i in range(self.roles_in_game[4])]
      #using generators to create any number of needed roles
		else:
      #exception handling 
			raise Exception("Number of roles Roles, must be possitive") #raise Error otherwise

		if hash_id_game is None:
			if hash_id_game not in Game.hash_used:
				self.hash = int(str(reduce(xor, [id(player) for player in Player.players]))[:7])
			else:
				self.hash = int(str(reduce(xor, [id(player) for player in Player.players]))[:6]+"0")
		else:
			self.hash = hash_id_game

		if map is None:
			try: # tries to load file
				self.map = r2Dtxt("map1.txt", "Files", r"Loading/Maps")
			except FileNotFoundError: #if file not found - loads this...
				self.map = Map(0, 0, [[loc1, loc1, loc3, loc3, loc11, loc14, loc14, loc14, loc1, loc1], [loc1, loc1, loc3, loc3, loc11, loc1, loc1, loc2, loc12, loc12], [loc2, loc15, loc15, loc11, loc11, loc7, loc7, loc12, loc12, loc9], [loc15, loc15, loc11, loc11, loc4, loc10, loc10, loc10, loc10, loc10], [loc6, loc11, loc11, loc8, l0c13, loc10, loc10, loc10, loc10, loc10], [loc11, loc11, loc5, loc8, loc13, loc10, loc2, loc10, loc10, loc10], [loc1, loc1, loc1, loc4, loc8, loc10, loc10, loc10, loc10, loc10], [loc3, loc3, loc3, loc3, loc15, loc15, loc15, loc5, loc4, loc11], [loc1, loc1, loc1, loc1, loc1, loc1, loc1, loc1, loc3, loc11], [loc14, loc2, loc14, loc10, loc10]])

											
	@staticmethod
	def random_role2human():
		position = randint(0, len(Player.players)-1)
		shuffle(Player.players)
		Player.players[position].is_human = True
		[human.role.discription for human in Player.players if human.is_human == True ]
    #Sets one human player and assigns a random role to the new human player.
   # [[(nightactions.discription()) for nightactions in player.role.possible_nightactions] for player in Player.players if player.is_human == True]

	@staticmethod
	def print_players():
		for pl in Player.players:
			if pl.is_alive:
				print(f"{pl.nick:>48} [{pl.role.name}] ({Player.players.index(pl)})--| Human-{pl.is_human}.")

	@staticmethod
	def morning():
		print("It's morning")
		[i.you_voted.Clear() for i in Player.alive_ingame_pl]
		[i.voted_for_you.Clear() for i in Player.alive_ingame_pl]
		# Just reseting voting

	@staticmethod
	def voting_phase():
		print("Please vote")
    #Player.players[0].role.possible_dayactions[0].voting_random()
		Player.voting_intellegent()
		print("Voting finnished")
    #Player.players[0].role.possible_dayactions[0].execution_random()
		Player.execution()

	@staticmethod
	def day():
		Game.morning()
		Game.voting_phase()

	@staticmethod
	def night():
		Player.doctor_visit()
		Player.sheriff_search()
		Player.assassin_kill()
		Player.mafia_kill()

	@staticmethod
	def first_night():
		Game.random_role2human()
		Game.print_players()

	def play():
		Game.first_night()
		while len(Player.alive_ingame_pl) > 3:
			roles_left = [pl.role for pl in Player.alive_ingame_pl]
			if assassin not in roles_left:
				if (roles_left.count(mafia)) >= (len(roles_left) - roles_left.count(mafia)):
					Game.game_running = False
					#Mafia wins
					for pl in Player.alive_ingame_pl:
						pl.points_l +=1 #All survived players get 1 point regurdless of win / loss.
					for pl in Player.players: #Scoring points (in objectives)
						if pl.role == mafia:
							pl.points_l +=4
							pl.games[0] +=1
							if pl.is_human:
								pl.points_l +=3
						else:
							pl.games[2] +=1
			elif Player.alive_ingame_pl.count(mafia) == 0: #Citizens win
				Game.game_running = False
				print("_______________________________")
				print("        Citizen victory!       ")
				print("_______________________________")
				for pl in Player.alive_ingame_pl:
					pl.points_l +=1
				for pl in Player.players:
					if pl.colour == COLOUR.RED:
						pl.points_l +=1
					

					
			Game.day()
			
			if len(Player.alive_ingame_pl) == 3:
				roles_left = [pl.role for pl in Player.alive_ingame_pl]
				if (mafia in roles_left):
					roles_left.remove(mafia)
					if (mafia in roles_left):
						Game.game_running = False #Mafia wins
						print("_______________________________")
						print("        Mafia victory!         ")
						print("_______________________________")
						for pl in Player.players: #Scoring points (in objectives)
							if pl.role == mafia:
								pl.points_l +=4
								pl.games[0] +=1
								if pl.is_human:
									pl.points_l +=3
								else:
									pl.games[2] +=1
				if len(Player.alive_ingame_pl) == 2:
					roles_left = [pl.role for pl in Player.alive_ingame_pl]
					if (mafia in roles_left) and (assassin in roles_left): #Mafia and assassin draws
						Game.game_running = False
						print("_______________________________")
						print("        Mafia victory!         ")
						print("        Assassin victory!      ")
						print("_______________________________")
						for pl in Player.players:
							pl.points_l += 3
							pl.games[0] +=1
							if pl.is_human:
								pl.points_l +=1
							else:
								pl.games[2] +=1
					elif (mafia in roles_left) and not (assassin in roles_left): #Mafia wins
						Game.game_running = False
						print("_______________________________")
						print("        Mafia victory!         ")
						print("_______________________________")
						for pl in Player.players:
							pl.points_l += 4
							pl.games[0] +=1
							if pl.is_human:
								pl.points_l +=3
							else:
								pl.games[2] +=1
					elif not (mafia in roles_left) and (assassin in roles_left): #Assassin wins
						Game.game_running = False
						print("_______________________________")
						print("        Assassin victory!      ")
						print("_______________________________")
						for pl in Player.players:
							pl.points_l += 3
							pl.games[0] +=1
							if pl.is_human:
								pl.points_l +=3
							else:
								pl.games[2] +=1
					else: #Citizens win
						Game.game_running = False
						print("_______________________________")
						print("        Citizen victory!       ")
						print("_______________________________")
						for pl in Player.alive_ingame_pl:
							pl.points_l +=1
						for pl in Player.players:
							if pl.colour == COLOUR.RED:
								pl.points_l +=1

			else:
				
				Game.night()
				
				if len(Player.alive_ingame_pl) > 3:
					roles_left = [pl.role for pl in Player.alive_ingame_pl]
					if (mafia in roles_left):
						roles_left.remove(mafia)
						if (mafia in roles_left):
							Game.game_running = False #Mafia wins
							
							for pl in Player.players: #Scoring points (in objectives)
								if pl.role == mafia:
									pl.points_l +=4
									pl.games[0] +=1
									if pl.is_human:
										pl.points_l +=3
									else:
										pl.games[2] +=1
				if len(Player.alive_ingame_pl) == 2:
					roles_left = [pl.role for pl in Player.alive_ingame_pl]
					if (mafia in roles_left) and (assassin in roles_left): #Mafia and assassin draws
						Game.game_running = False
						print("_______________________________")
						print("        Mafia victory!         ")
						print("        Assassin victory!      ")
						print("_______________________________")
						for pl in Player.players:
							pl.points_l += 3
							pl.games[0] +=1
							if pl.is_human:
								pl.points_l +=1
							else:
								pl.games[2] +=1
					elif (mafia in roles_left) and not (assassin in roles_left): #Mafia wins
						Game.game_running = False
						print("_______________________________")
						print("        Mafia victory!         ")
						print("_______________________________")
						for pl in Player.players:
							pl.points_l += 4
							pl.games[0] +=1
							if pl.is_human:
								pl.points_l +=3
							else:
								pl.games[2] +=1
					elif not (mafia in roles_left) and (assassin in roles_left): #Assassin wins
						Game.game_running = False
						print("_______________________________")
						print("        Assassin victory!      ")
						print("_______________________________")
						for pl in Player.players:
							pl.points_l += 3
							pl.games[0] +=1
							if pl.is_human:
								pl.points_l +=3
							else:
								pl.games[2] +=1
					else: #Citizens win
						Game.game_running = False
						print("_______________________________")
						print("        Citizen victory!       ")
						print("_______________________________")
						for pl in Player.alive_ingame_pl:
							pl.points_l +=1
						for pl in Player.players:
							if pl.colour == COLOUR.RED:
								pl.points_l +=1

	@staticmethod
	def run():
		while True:
			print("_______________________________")
			print("     Welcome to Mafia Game!    ")
			print()
			print("So here's what you can do:\n")
			print("Press (p) to Play")
			print("Press (h) to open help section")
			print("Press (q) to Quit")

			user_choice = input("What do you choose:\n")
			if user_choice.lower() == "q":
				print("Game quitted")
				break
			elif user_choice.lower() == "h":
				print("Help Menu:")
				print("\t\tRules:")
				print("Mafia is a team game played conditionally by 2 teams: civilians against the mafia. The goal of the game is to win with your team and at the same time (preferably) stay alive. The task of civilians is to identify mafia players and put them to death. The mafia players have to impersonate ordinary residents and capture the city, destroying all honest citizens. At night, honest citizens sleep (with the exception of active roles - the sheriff, doctor and assassin, who play on the side of civilians), and the mafia chooses a victim.")
				print("During the day, any player can express their true (or imaginary) suspicions against any player, accusing him of having connections with the mafia and putting his candidacy to the vote. After voting is completed, the player with the most votes is given the final say after which they are excecuted")
				
				print("Then night comes again. And again, the mafia chooses the next victim, who will be found dead in the morning if the doctor or the sheriff do not come to the rescue in time. Alone, this decision has to be made by a assassin, only his task is to find members of the mafia or betray the civillians. And so on until the end. The game ends either with the complete victory of the mafia or civilians. In the event that an equal number of players remain on both sides, it is considered that the mafia has won. As you probably already understood, in the game Mafia, like in the card game Poker, there are two components: the ability to observe other people and the ability to draw conclusions about the strategies that other players play.")
							
				print("\t\tCitizen Roles:")
				print(citizen.discription)
				print(mafia.discription)
				print(assassin.discription)
				print(sheriff.discription)
				print(doctor.discription)
				
			elif user_choice.lower() == "p":
				Game.play()
			
  

    
  



  


