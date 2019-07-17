
import tkinter as tk
import time

# Routine for non-implemented features.
def NOTIMPLEMENTED():
	print(">>> Not implemented <<<")

# Simulate the face buttons.
class MicrobitButton(tk.Button):
	def setup(self):
		self.presses = 0
		self.state = False
		self.bind("<Button-1>", self.bpress)
		self.bind("<ButtonRelease-1>", self.bunpress)

	def get_presses(self):
		return self.presses

	def is_pressed(self):
		return self.state

	def bpress(self,x):
		self.state = True

	def bunpress(self,x):
		self.state = False
		self.increment()

	def increment(self):
		self.presses = self.presses + 1

class Image:
	def __init__(self):
		self.data = [x[:] for x in [[0] * 5] * 5]

	def __init__(self, image_data):
		self.data = [x[:] for x in [[0] * 5] * 5]
		if type(image_data) is str:
			if len(image_data) == 1:
				NOTIMPLEMENTED()
			else:
				NOTIMPLEMENTED()
		else:
			for j in range(5):
				for i in range(5):
					self.data[i][j] = int(image_data[j][i])

class ledpack:
	def __init__(self, canvas, context):
		self.context = context
		self.leds = [x[:] for x in [[0] * 5] * 5]
		self.canvas = canvas
		self.draw_leds()
		self.turnedon=True
		

	def draw_leds(self):
		self.canvas.create_rectangle(0,0,200,200,fill='black')
		for i in range(5):
			for j in range(5):
				if self.leds[i][j] >= 1:
					shade = hex(int((self.leds[i][j] * 32) - 1))[2:]
					if len(shade) == 1:
						shade = "0" + shade
					shade = "#" + shade + "0000"
					self.canvas.create_rectangle(i*40,j*40,(i+1)*40,(j+1)*40,fill=shade)
		self.canvas.update_idletasks()
		self.context.update()
		

	def set_pixel(self, x, y, value):
		self.leds[x][y] = value
		self.draw_leds()

	def get_pixel(self, x, y):
		return self.leds[x][y]

	def clear(self):
		self.leds = [x[:] for x in [[0] * 5] * 5]
		self.draw_leds()

	def on(self):
		self.turnedon = True

	def off(self):
		self.turnedon = False

	def is_on(self):
		return self.turnedon

	def read_light_level(self):
		NOTIMPLEMENTED()
		return 0

	def scroll(self, value, delay=400, wait=True, loop=False, monospace=False):
		NOTIMPLEMENTED()

	def show(self, image):
		for i in range(5):
			for j in range(5):
				self.leds[i][j] = image.data[i][j]
		self.draw_leds()
		


# Set up stuff when imported.
_mb_win = tk.Tk()
_mb_win.title("Macro:Bit")

button_a = MicrobitButton(_mb_win, text="A")
button_b = MicrobitButton(_mb_win, text="B")
button_a.setup()
button_b.setup()
button_a.pack(side=tk.LEFT)
button_b.pack(side=tk.RIGHT)
_mb_can = tk.Canvas(_mb_win, width=200, height=200)
display = ledpack(_mb_can, _mb_win)
_mb_can.pack(expand=tk.YES, fill=tk.BOTH) 