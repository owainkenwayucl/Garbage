COLOURS=" ░▒▓█"

def show(data, x, y, colours=COLOURS):
	num_colours=len(colours)
	mx = max(data)
	mn = min(data)
	rn = mx - mn
	for a in range(y):
		for b in range(x):
			v = (data[a][b] - mn)/rn
				
			quantised = int(v * num_colours)
			if quantised >= len(colours):
				quantised = len(colours - 1)

			print(colours[quantised], end='')
		print("")
			
