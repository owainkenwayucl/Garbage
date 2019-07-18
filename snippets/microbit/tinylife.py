# Tiny implementation of Conway's game of life, eventually destined for upython
# on the BBC Micro:Bit

# Owain Kenway

# Images are always 5x5 as we want to show them on the LEDs.
xres = 5
yres = 5

from microbit import *

def life(image, console=False, printpop=False):
	p = button_a.get_presses()
	# Our main loop.
	while (True):
		if button_a.get_presses() > p:
			break
		
		imstr = "" # Structure for uPython Micro:Bit images
		pop = 0 # Keep track of population
		newimage = blank()
		if (console):
			print("+-----+")
		# Output last step and update current.
		for j in range(yres):
			if (console):
				print("|", end="")
			for i in range(xres):
				if image[i][j] == 1:
					if (console):
						print("#",end="")
					pop += 1
					imstr = imstr + "8"
				else:
					if (console):
						print(" ",end="")
					imstr = imstr + "0"

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
			if (console):
				print("|")
			imstr = imstr + ":"
		imstr = imstr[:-1]
		if (console):
			print("+-----+")
		if (printpop):
			print("Population: " + str(pop))
		#if pop <= 0:
		#	break
		if (console):
			print("")

		outimg = Image(imstr)  # Create Micro:Bit image
		display.show(outimg)   # Push it to LEDs.

		# Copy new image into old.
		for j in range(yres):
			for i in range(xres):
				image[i][j] = newimage[i][j]


# Create a glider input.
def glider():
	image = blank()

	# set up glider
	image[3][1] = 1
	image[1][2] = 1
	image[3][2] = 1
	image[2][3] = 1
	image[3][3] = 1

	return(image)

def randomp(p):
	import random
	r = [x[:] for x in [[0] * yres] *xres]
	for i in range(5):
		for j in range(5):
			n = random.random()
			if n <= p:
				r[i][j] = 1
	return r

def blank():
	return [x[:] for x in [[0] * yres] *xres]


