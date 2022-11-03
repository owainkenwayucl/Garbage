COLOURS=' ░▒▓█'
ASCII_COLOURS=' .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
EMOJI_COLOURS=['️⬛','🟫','🟧','🟥','🟪','🟦','🟩','🟨️','⬜']


def show(data, colours=COLOURS):
	height = len(data)
	num_colours=len(colours)
	for a in range(height):
		width = len(data[a])
		for b in range(width):
			v = data[a][b]
				
			quantised = int(v * (num_colours-1))

			print(colours[quantised], end='')
		print("")
			
