from enum import Enum


class Difficulty(Enum):
	EASY = 1
	NORMAL = 2
	HARD = 3


def get_tick_rate(difficulty: Difficulty) -> int:
	"""Return updates per second for the given difficulty.

	Frontend should convert this to pygame clock FPS. Keeping logic here
	allows backend to be tested without pygame.
	"""
	if difficulty == Difficulty.EASY:
		return 6
	if difficulty == Difficulty.NORMAL:
		return 10
	if difficulty == Difficulty.HARD:
		return 14
	return 10

