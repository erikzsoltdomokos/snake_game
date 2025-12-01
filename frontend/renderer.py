import pygame
from typing import Tuple


class Renderer:
	"""Responsible purely for drawing the game state using pygame."""

	def __init__(self, surface: pygame.Surface, cell_size: int = 20):
		self.surface = surface
		self.cell_size = cell_size
		self.font = pygame.font.SysFont("consolas", 20)

		# Themes: mud-like dark and light vibrant
		self.themes = {
			"mud": {
				"bg1": (39, 34, 28),
				"bg2": (44, 38, 31),
				"snake": (86, 137, 66),
				"head": (70, 120, 55),
				"food": (220, 50, 50),
				"food_shadow": (110, 25, 25),
				"grid": (48, 42, 35),
				"text": (230, 225, 215),
			},
			"vibrant": {
				"bg1": (22, 24, 36),
				"bg2": (28, 30, 44),
				"snake": (80, 200, 120),
				"head": (60, 180, 110),
				"food": (250, 100, 100),
				"food_shadow": (120, 40, 40),
				"grid": (40, 40, 52),
				"text": (240, 240, 240),
			},
		}
		self.colors = self.themes["mud"]
		self.theme_name = "mud"

	def draw_grid(self, grid_size: Tuple[int, int]):
		w, h = grid_size
		# Checkerboard-like subtle background
		self.surface.fill(self.colors["bg1"])
		for y in range(h):
			for x in range(w):
				if (x + y) % 2 == 0:
					rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
					self.surface.fill(self.colors["bg2"], rect)

	def draw_snake(self, body):
		for i, (x, y) in enumerate(body):
			color = self.colors["head"] if i == 0 else self.colors["snake"]
			rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
			# Slight rounded corners and outline for a cleaner look
			pygame.draw.rect(self.surface, color, rect, border_radius=self.cell_size // 4)
			pygame.draw.rect(self.surface, (20, 20, 26), rect, width=2, border_radius=self.cell_size // 4)

	def draw_food(self, food):
		x, y = food
		rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
		# Draw apple: circle with leaf and shadow
		shadow = rect.copy()
		shadow.x += 2
		shadow.y += 2
		pygame.draw.ellipse(self.surface, self.colors["food_shadow"], shadow)
		pygame.draw.ellipse(self.surface, self.colors["food"], rect)
		# leaf
		leaf_rect = pygame.Rect(rect.x + rect.width * 0.6, rect.y - rect.height * 0.15, rect.width * 0.3, rect.height * 0.3)
		pygame.draw.ellipse(self.surface, (60, 160, 80), leaf_rect)

	def draw_hud(self, score: int, paused: bool = False):
		text = self.font.render(f"Score: {score}", True, self.colors["text"])
		self.surface.blit(text, (8, 8))
		if paused:
			pause_txt = self.font.render("Paused (P)", True, (200, 200, 120))
			self.surface.blit(pause_txt, (8, 32))

	def draw_pause_overlay(self):
		"""Draw a styled pause overlay in the center of the screen."""
		small_font = pygame.font.SysFont("consolas", 22)
		title_font = pygame.font.SysFont("consolas", 32, bold=True)
		
		# Semi-transparent dark overlay
		overlay = pygame.Surface(self.surface.get_size(), pygame.SRCALPHA)
		overlay.fill((10, 10, 14, 200))
		self.surface.blit(overlay, (0, 0))
		
		# Draw centered box
		box_w, box_h = 360, 240
		box_x = (self.surface.get_width() - box_w) // 2
		box_y = (self.surface.get_height() - box_h) // 2
		box_rect = pygame.Rect(box_x, box_y, box_w, box_h)
		
		# Box background and border
		pygame.draw.rect(self.surface, (30, 32, 40), box_rect, border_radius=12)
		pygame.draw.rect(self.surface, (80, 80, 100), box_rect, width=2, border_radius=12)
		
		# Title
		title = title_font.render("PAUSED", True, (240, 240, 240))
		title_rect = title.get_rect(center=(box_x + box_w // 2, box_y + 40))
		self.surface.blit(title, title_rect)
		
		# Instructions
		instructions = [
			"P: Resume",
			"T: Toggle theme",
			"Esc: Quit to menu"
		]
		y_offset = box_y + 90
		for line in instructions:
			txt = small_font.render(line, True, (200, 200, 200))
			txt_rect = txt.get_rect(center=(box_x + box_w // 2, y_offset))
			self.surface.blit(txt, txt_rect)
			y_offset += 35

	def render(self, state, paused: bool = False) -> None:
		"""Draw the entire frame based on backend `state`."""
		self.draw_grid(state.grid_size)
		self.draw_snake(state.snake.body)
		self.draw_food(state.food)
		if state.bonus_food:
			self.draw_food(state.bonus_food)
		self.draw_hud(state.score, paused=paused)
		if paused:
			self.draw_pause_overlay()

	def toggle_theme(self):
		self.theme_name = "vibrant" if self.theme_name == "mud" else "mud"
		self.colors = self.themes[self.theme_name]

