from dataclasses import dataclass
from typing import List, Tuple


Point = Tuple[int, int]


@dataclass
class Snake:
	"""List-based snake model.

	- body[0] is head.
	- direction is one of (dx, dy) with unit steps on grid.
	- grid uses integer coordinates.
	"""
	body: List[Point]
	direction: Point
	grow_pending: int = 0

	def set_direction(self, new_dir: Point) -> None:
		"""Set movement direction, disallow 180-degree turn.

		A 180° turn would cause immediate self-collision; we prevent that.
		"""
		ndx, ndy = new_dir
		cdx, cdy = self.direction
		if (ndx, ndy) == (-cdx, -cdy):
			return
		if (ndx, ndy) == (0, 0):
			return
		self.direction = (ndx, ndy)

	def next_head(self) -> Point:
		hx, hy = self.body[0]
		dx, dy = self.direction
		return (hx + dx, hy + dy)

	def move(self) -> None:
		"""Advance snake by one step, applying growth if pending."""
		new_head = self.next_head()
		self.body.insert(0, new_head)
		if self.grow_pending > 0:
			self.grow_pending -= 1
		else:
			self.body.pop()

	def grow(self, amount: int = 1) -> None:
		self.grow_pending += max(0, amount)

