from enum import Enum

class Colour(Enum):
  RED = 0
  BLUE = 1
  BLACK = 3
  PINK = 4
  CYAN = 5
  GRAY = 6
  WHITE = 7
  NO_COLOUR = "NO COLOUR"

  def change_color(person, colour):
    person.colour = colour
  
