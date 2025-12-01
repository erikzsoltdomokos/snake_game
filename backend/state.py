from dataclasses import dataclass
from typing import Tuple, Optional

from .snake import Snake
from .food import spawn_food
from .collision import is_out_of_bounds, hits_self
from .difficulty import Difficulty
import random


@dataclass
class GameState:
	"""Holds full game state independent of pygame.

	Grid is logical in cells; frontend maps to pixels.
	"""
	grid_size: Tuple[int, int]
	difficulty: Difficulty
	snake: Snake
	food: Tuple[int, int]
	score: int = 0
	running: bool = True
	wrap_edges: bool = False
	rng: random.Random = random.Random()
	bonus_food: Optional[Tuple[int, int]] = None
	bonus_timer: int = 0

	@staticmethod
	def new(grid_size: Tuple[int, int], difficulty: Difficulty, *, wrap_edges: bool = False, seed: Optional[int] = None) -> "GameState":
		w, h = grid_size
		start = (w // 2, h // 2)
		snake = Snake(body=[start], direction=(1, 0))
		rng = random.Random(seed) if seed is not None else random.Random()
		food = spawn_food(grid_size, occupied=snake.body)
		return GameState(grid_size=grid_size, difficulty=difficulty, snake=snake, food=food, wrap_edges=wrap_edges, rng=rng)

	def update(self) -> None:
		"""Advance the game by one tick.

		- Moves snake
		- Checks collisions
		- Handles food consumption and growth
		"""
		if not self.running:
			return

		next_head = self.snake.next_head()
		w, h = self.grid_size
		if self.wrap_edges:
			x, y = next_head
			next_head = (x % w, y % h)

		# Collision pre-check (optional optimization)
		if not self.wrap_edges and is_out_of_bounds(next_head, self.grid_size):
			self.running = False
			return

		# Move snake
		# Move snake (direction already set). If wrap, we manually insert head and pop tail
		if self.wrap_edges:
			# manual move to respect wrapped next_head
			self.snake.body.insert(0, next_head)
			if self.snake.grow_pending > 0:
				self.snake.grow_pending -= 1
			else:
				self.snake.body.pop()
		else:
			self.snake.move()

		# Post-move checks
		head = self.snake.body[0]
		if hits_self(head, self.snake.body):
			self.running = False
			return

		# Food
		if head == self.food:
			self.score += 1
			self.snake.grow(self._growth_amount())
			self.food = spawn_food(self.grid_size, occupied=self.snake.body)
			# chance to spawn bonus food
			if self.bonus_food is None and self.rng.random() < 0.25:
				self.bonus_food = spawn_food(self.grid_size, occupied=self.snake.body)
				self.bonus_timer = 50  # ticks

		# bonus food logic
		if self.bonus_food:
			if head == self.bonus_food:
				self.score += 3
				self.snake.grow(self._growth_amount() + 1)
				self.bonus_food = None
				self.bonus_timer = 0
			else:
				self.bonus_timer -= 1
				if self.bonus_timer <= 0:
					self.bonus_food = None
					self.bonus_timer = 0

	def _growth_amount(self) -> int:
		if self.difficulty == Difficulty.EASY:
			return 2
		if self.difficulty == Difficulty.NORMAL:
			return 1
		return 1

