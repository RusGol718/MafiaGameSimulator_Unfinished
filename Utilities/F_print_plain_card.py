def draw_plain_card(height, width):
	card = []
	top = "_"*(width)
	middle = "|" + " " * (width-2) + "|"
	bottom = "|" + "_"*(width-2) + "|"
	card.append(top)
	for height_without_top_bottom in range(height - 2):
		card.append(middle)
	card.append(bottom)
	return card


def draw_plain_grid(height, width):
	raw_grid = []
	top = "_"* (2*width+1)
	between = "–"* (2*width+1)
	middle = ("| " * (width + 1))[:-1]
	raw_grid.append(top)
	for height_without_top_bottom in range(height):
		raw_grid.append(middle)
		raw_grid.append(between)
	return raw_grid




def print_plain_card(card):
	for i in card:
		print(i)