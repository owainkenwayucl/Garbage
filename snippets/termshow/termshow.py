COLOURS=" ░▒▓█"

def show(colours=COLOURS, data, x, y):
	num_colours=len(colours)
	for a in range(y):
		for b in range(x):
			quantised = int(data[a][b] * num_colours)
			print(colours[quantised], end='')
		print("")
			
