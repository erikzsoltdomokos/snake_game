import pygame


class InputHandler:
	"""Process keyboard input and map to backend snake direction changes."""

	def __init__(self):
		# No state for now; could add pause, etc.
		pass

	def process_events(self, state, paused: bool) -> tuple[bool, bool]:
		"""Handle events.

		Returns (continue_running, paused_state).
		"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False, paused
			if event.type == pygame.KEYDOWN:
				if event.key in (pygame.K_ESCAPE, pygame.K_q):
					return False, paused
				if event.key == pygame.K_p:
					paused = not paused
					return True, paused
				if event.key == pygame.K_t:
					# Theme switch: frontend only, accessed via state via renderer elsewhere
					# We'll signal via setting an attribute for renderer usage (handled in loop)
					paused = paused  # no change; theme will be toggled in loop
					return True, paused
				if event.key in (pygame.K_UP, pygame.K_w):
					state.snake.set_direction((0, -1))
				elif event.key in (pygame.K_DOWN, pygame.K_s):
					state.snake.set_direction((0, 1))
				elif event.key in (pygame.K_LEFT, pygame.K_a):
					state.snake.set_direction((-1, 0))
				elif event.key in (pygame.K_RIGHT, pygame.K_d):
					state.snake.set_direction((1, 0))
		return True, paused

