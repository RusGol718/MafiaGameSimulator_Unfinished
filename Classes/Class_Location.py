from Utilities.F_reading_json import reading_json as rjson
from Utilities.F_writing_json import writing_json as wjson

class Location:
	locations = []
	
	try: # tries to load file
		loc_dict = rjson("locations_dict.json", "Files", r"Loading/Maps")
	except FileNotFoundError: #if file not found - loads this...
		loc_dict = {
		  "-" : "Street",
		  "B" : "Bloodbath",
		  "^" : "House",
		  "P" : "Police station",
		  "+" : "Hospital",
		  "$" : "Bank",
		  "H" : "Hotel",
		  "~" : "Bar",
		  "Z" : "Zoo", 
		  "O" : "Office block",
		  "=" : "Railway",
		  "C" : "College",
		  "T" : "Town centre", 
		  "#" : "Graveyard", 
		  "@" : "Apartment complex"
		}

	def __init__(self, key):
		self.key = key
		self.x = 0
		self.y = 0
		try:
			self.name = Location.loc_dict[key]
		except KeyError:
			new_loc_valid = input("Hey there! There is no location with this key. But who cares! You can create your own\n Want to proceed? (y/n)")

			while new_loc_valid.lower() != "y":
				if new_loc_valid.lower() == "n":
					self.key = "-"
					self.name = Location.loc_dict["-"]
					break
				else:
					new_loc_valid = input("Please enter y/n to continue	  ")
			else:
				print(f"Ok. So we're using the key that you entered to create a new location. {key}")
				new_loc_name = input("Please enter a new location	")
				Location.loc_dict[key] = new_loc_name
				self.name = new_loc_name
		else:
			self.name = Location.loc_dict[key]
		finally:
			wjson(Location.loc_dict, "locations_dict.json", "Files", "Loading/Maps")
		Location.locations.append(self)
		



loc1 = Location("-")
loc2 = Location("B")
loc3 = Location("^")
loc4 = Location("P")
loc5 = Location("+")
loc6 = Location("$")
loc7 = Location("H")
loc8 = Location("~")
loc9 = Location("Z")
loc10 = Location("O")
loc11 = Location("=")
loc12 = Location("C")
loc13 = Location("T")
loc14 = Location("#")
loc15 = Location("@")
loc_pl = Location("X")
#print(Location.locations)
