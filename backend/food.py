import random
from typing import List, Tuple

Point = Tuple[int, int]


def spawn_food(grid_size: Tuple[int, int], occupied: List[Point]) -> Point:
	"""Place food at a random free grid cell, avoiding occupied cells.

	If grid is full, returns the head position (no-op); caller can decide behavior.
	"""
	w, h = grid_size
	all_cells = [(x, y) for x in range(w) for y in range(h)]
	free = [p for p in all_cells if p not in occupied]
	if not free:
		return occupied[0] if occupied else (0, 0)
	return random.choice(free)

