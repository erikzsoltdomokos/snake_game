from typing import List, Tuple

Point = Tuple[int, int]


def is_out_of_bounds(point: Point, grid_size: Tuple[int, int]) -> bool:
	x, y = point
	w, h = grid_size
	return x < 0 or y < 0 or x >= w or y >= h


def hits_self(head: Point, body: List[Point]) -> bool:
	# body includes head at index 0; check duplicates from index 1
	return head in body[1:]

