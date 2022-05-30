from random import randint as rint

from Classes.Class_Location import *
from Utilities.F_print_plain_card import draw_plain_grid as draw
from Utilities.F_reading_json import reading_json as rjson
from Utilities.F_writing_json import writing_json as wjson


class Map():
    def __init__(self, width, height, predefined_grid:list=None):
        self.x = width
        self.y = height
        if predefined_grid is None:
            self.grid_map = [[" " for y in range(self.y)] for x in range(self.x)]
        else:
            self.grid_map = predefined_grid
            self.x = max([len(i) for i in predefined_grid])
            columns_transposed = [[i[j] for i in predefined_grid] for j in range(min([len(i) for i in predefined_grid]))]
            self.y = max([len(i) for i in columns_transposed])

    def __len__(self):
        return self.x * self.y # returns area of the grid using/replacing the magic method len() 

    def __str__(self):
        str_map = ""
        for i in self.setup_str_map(self.grid_map):
            str_map += i + "\n"
        return str_map

    @staticmethod
    def loading_loc_dict():
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
		
				

    def traspose(self):
        return [[i[j] for i in self.grid_map] for j in range(min([len(i) for i in self.grid_map]))]
        
        # Transposes the matrix grid or in other words relects coordinates by y=-x (the main diagonal)
    def setup_str_map(self, array_grid_2d:list=None):
        
        complete_map = []
        row_string = ""
        raw_map = draw(self.y, self.x)# create a template
        if array_grid_2d is None:
            for i, j in zip(raw_map[1::2], self.grid_map): # iterate through odd to miss lines
                for k, l in zip(i[1::2], j): # iterate throught to get to blanks 
                    if type(l) == Location:
                        l = l.key
                    row_string = row_string + "|"+ l #cummulativly add | and new symbol  in grid
                    if len(row_string) == 2 * len(self.grid_map[0]):
                        # if maximum length of 1 row is exceeded resets the string and appends it to a new 2d grid text based
                        complete_map.append(row_string)
                        row_string = ""
        else: # same code but with a custom 2d grid
            if type(array_grid_2d) == list:
                for i, j in zip(raw_map[1::2], array_grid_2d):
                    for k, l in zip(i[1::2], j):
                        if type(l) == Location:
                            l = l.key
                        row_string = row_string + "|"+ l
                        if len(row_string) == 2 * len(array_grid_2d[0]):
                            complete_map.append(row_string)
                            row_string = ""

        complete_map = [i+"|" for i in complete_map]
        # Adds | at the end of each row to close the grid
        complete_map.insert(0, raw_map[0])
        # Adds the _(underscode) symbols to close the grid at the top
        [complete_map.insert(2*i+2, raw_map[2]) for i in range(len(raw_map)//2)]
        #Adds the (–) extended dash symbols between the values to form a grid
        
        return complete_map
                            
    
    def set_locations(self, num_players):
        random_cood_pl = (rint(0, len(self.grid_map)-1), rint(0, len(self.traspose())-1))
        repeats = []
        counter = 0
        while counter-1 != num_players:
          if random_cood_pl not in repeats:
            self.grid_map[random_cood_pl[0]][random_cood_pl[1]] = loc_pl
            random_cood_pl = (rint(0, len(self.grid_map)-1), rint(0, len(self.traspose())-1))
            counter +=1
          
        return self.grid_map


map1 = Map(0, 0, [[loc1, loc1, loc3, loc3, loc11, loc14, loc14, loc14, loc1, loc1], [loc1, loc1, loc3, loc3, loc11, loc1, loc1, loc2, loc12, loc12], [loc2, loc15, loc15, loc11, loc11, loc7, loc7, loc12, loc12, loc9], [loc15, loc15, loc11, loc11, loc4, loc10, loc10, loc10, loc10, loc10], [loc6, loc11, loc11, loc8, loc13, loc10, loc10, loc10, loc10, loc10], [loc11, loc11, loc5, loc8, loc13, loc10, loc2, loc10, loc10, loc10], [loc1, loc1, loc1, loc4, loc8, loc10, loc10, loc10, loc10, loc10], [loc3, loc3, loc3, loc3, loc15, loc15, loc15, loc5, loc4, loc11], [loc1, loc1, loc1, loc1, loc1, loc1, loc1, loc1, loc3, loc11], [loc14, loc2, loc14, loc10, loc10]])