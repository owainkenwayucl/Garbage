# Tiny implementation of Conway's game of life, eventually destined for upython
# on the BBC Micro:Bit

# Owain Kenway

# Images are always 5x5 as we want to show them on the LEDs.
xres = 5
yres = 5

def life(image):
	# Our main loop.
	while (True):
		pop = 0 # Keep track of population
		newimage=[x[:] for x in [[0] * yres] *xres]
		print("+-----+")
		# Output last step and update current.
		for j in range(yres):
			print("|", end="")
			for i in range(xres):
				if image[i][j] == 1:
					print("#",end="")
					pop += 1
				else:
					print(" ",end="")

				orig = image[i][j]
				left = (i-1)%xres
				right = (i+1)%xres
				above = (j-1)%yres
				below = (j+1)%yres

				# 9 way sum.
				s = (image[left][above] + image[i][above] + image[right][above] + image[left][j] + image[i][j] + image[right][j] + image[left][below] + image[i][below] + image[right][below])
				if (s == 3):
					newimage[i][j] = 1
				elif (s == 4):
					newimage[i][j] = orig
				else:
					newimage[i][j] = 0
			print("|")
		print("+-----+")
		print("Population: " + str(pop))
		print("")
		# Copy new image into old.
		for j in range(yres):
			for i in range(xres):
				image[i][j] = newimage[i][j]


# Create a glider input.
def glider():
	image = [x[:] for x in [[0] * yres] *xres]

	# set up glider
	image[3][1] = 1
	image[1][2] = 1
	image[3][2] = 1
	image[2][3] = 1
	image[3][3] = 1

	return(image)

life(glider())
