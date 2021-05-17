from random import SystemRandom
random = SystemRandom()
def black_pattern_generate():
	block = random.randint(0, 4)
	row = random.randint(0, 4)
	if block == row:
		return (1, 1, 1, 1)
	else:
		return (0, 0, 0, 0)

# print(black_pattern_generate(2, 2))

white = []

white += [
		(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)
	]

white += [
		(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 0, 0)
	]

white += [
		(0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 0, 0), (0, 1, 0, 0)
	]

white += [
		(0, 0, 0, 1), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)
	]

def white_pattern_generate():
	return random.choice(white)


# print(white_pattern_generate())
# print(white)
