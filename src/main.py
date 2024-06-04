import mido
import pygame
import math

# Shared Variables
state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # [C, ... ,B]
sustain_on = False

# Pygame Variables
width, height = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = None
# Circle parameters
center = (width // 2, height // 2)
radius = 300
thickness = 5
notes_fifths = ["C", "G", "D", "A", "E", "B", "F#", "Db", "Ab", "Eb", "Bb", "F"]


def process_message(msg):
	"""
	Process Message coming in from midi port
	written as a callback to be used with mido.open_port()
	"""
	print(msg)
	# TODO -> Implement this callback function that will be used to process midi messages from mido


def draw_screen():
	"""
	use global variables to draw out the circle of fifths
	"""
	pygame.draw.circle(screen, BLACK, center, radius, thickness)

	# TODO -> use the state and sustain_on variables to highlight the notes that are pressed

	for i, note in enumerate(notes_fifths):
		angle = math.radians(360 / len(notes_fifths) * i)
		x = center[0] + radius * math.cos(angle)
		y = center[1] + radius * math.sin(angle)
		text = font.render(note, True, BLACK)
		text_rect = text.get_rect(center=(x, y))
		screen.blit(text, text_rect)

def init_midi_keyboard():
	"""
	Look for midi device, and use it
	"""
	pass
	# TODO -> implement midi keyboard initalization code for midi device

if __name__ == "__main__":
	# initalize pygame window
	pygame.init()
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Music Visualizer")
	font = pygame.font.SysFont('Arial', 24)

	# initlize midi keyboard
	# TODO -> implement midi keyboard initalization code for midi device
	# device_index = init_midi_keyboard()
	# input_names = mido.get_input_name()
	# input = mido.open_input(input_names[device_index], callback=process_message)

	# Game Loop
	running = True
	while running:
		
		# check if user hits the window close button
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# fill in background
		screen.fill((255, 255, 255))
		
		# draw out screen based on state
		draw_screen()

		# finalize frame
		pygame.display.flip()

	pygame.quit()
	
