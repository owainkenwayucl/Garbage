COLOURS=" ░▒▓█"

def show(data, x, y, colours=COLOURS):
	num_colours=len(colours)
	for a in range(y):
		for b in range(x):
			v = data[a][b]
				
			quantised = int(v * num_colours)
			if quantised >= len(colours):
				quantised = len(colours) - 1

			print(colours[quantised], end='')
		print("")
			
