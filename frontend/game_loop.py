import pygame
from typing import Tuple

from backend.state import GameState
from backend.difficulty import Difficulty, get_tick_rate
from .renderer import Renderer
from .input_handler import InputHandler
from .sound_manager import SoundManager


def run_game(grid_size: Tuple[int, int], difficulty: Difficulty, cell_size: int = 20, wrap_edges: bool = False, start_fullscreen: bool = False) -> tuple[int, bool]:
	"""Run the pygame loop. Returns final score."""
	pygame.init()
	width, height = grid_size
	base_size = (width * cell_size, height * cell_size)
	flags = pygame.FULLSCREEN if start_fullscreen else 0
	screen = pygame.display.set_mode(base_size if not start_fullscreen else (0, 0), flags)
	pygame.display.set_caption("Snake")

	clock = pygame.time.Clock()
	# Render onto an offscreen surface (logical size), then scale to window/fullscreen
	render_surface = pygame.Surface(base_size)
	renderer = Renderer(render_surface, cell_size=cell_size)
	inputs = InputHandler()
	sound_manager = SoundManager()

	state = GameState.new(grid_size, difficulty, wrap_edges=wrap_edges)

	tick_rate = get_tick_rate(difficulty)

	running = True
	paused = False
	prev_score = state.score
	prev_bonus = None
	theme_toggle = False
	fullscreen = bool(start_fullscreen)
	f_key_prev = False
	while running and state.running:
		running, paused = inputs.process_events(state, paused)
		# Poll theme toggle (key T) using pygame directly to keep frontend concerns here
		keys = pygame.key.get_pressed()
		if keys[pygame.K_t] and not theme_toggle:
			renderer.toggle_theme()
			theme_toggle = True
		if not keys[pygame.K_t]:
			theme_toggle = False

		# Fullscreen toggle with F, and scale the render surface accordingly
		if keys[pygame.K_f] and not f_key_prev:
			fullscreen = not fullscreen
			flags = pygame.FULLSCREEN if fullscreen else 0
			screen = pygame.display.set_mode((0, 0) if fullscreen else base_size, flags)
		f_key_prev = keys[pygame.K_f]

		# Advance backend logic only if not paused
		if not paused:
			before_running = state.running
			state.update()
			# Sound events
			if state.score > prev_score:
				# Check if bonus was eaten
				if prev_bonus and not state.bonus_food:
					sound_manager.play('bonus')
				else:
					sound_manager.play('eat')
			if before_running and not state.running:
				sound_manager.play('die')
			prev_score = state.score
			prev_bonus = state.bonus_food

		# Draw
		renderer.render(state, paused=paused)
		# Scale and blit to actual screen
		screen_size = screen.get_size()
		if screen_size != base_size:
			scaled = pygame.transform.smoothscale(render_surface, screen_size)
			screen.blit(scaled, (0, 0))
		else:
			screen.blit(render_surface, (0, 0))
		pygame.display.flip()

		# Control speed (FPS)
		clock.tick(tick_rate)

	# End screen simple display
	font = pygame.font.SysFont("consolas", 28)
	overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
	overlay.fill((10, 10, 14, 180))
	screen.blit(overlay, (0, 0))
	text = font.render(f"Game Over - Score: {state.score}", True, (240, 240, 240))
	screen.blit(text, (10, 10))
	pygame.display.flip()

	# brief pause before returning to caller (menu)
	pygame.time.delay(800)
	return state.score, fullscreen

