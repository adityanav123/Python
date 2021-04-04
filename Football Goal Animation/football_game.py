import pygame
import random
import math

# initialise game
pygame.init()

#creating screen
screen = pygame.display.set_mode((600, 764))

# background
background = pygame.image.load('ground.png')

# title
pygame.display.set_caption('Football Goal')
icon = pygame.image.load('soccer-ball.png')
pygame.display.set_icon(icon)

# ball
ballImage = pygame.image.load('ball.png')
ballX = 300
ballY = 350
ballChangeX = 0
ballChangeY = 0

# player - red
playerRedImage = [pygame.image.load('red.png')] * 3
playerRedX = []
playerRedY = []

# one player should always be in the inner box.
playerRedX.append(random.randint(100, 500)) ## just for checking.
playerRedY.append(random.randint(100, 140))

# rest players are randomised.
for i in range(2):
	playerRedX.append(random.randint(100, 500))
	playerRedY.append(random.randint(160, 350))


# blue players
playerBlueImage = [pygame.image.load('blue.png')] * 4
playerBlueX = []
playerBlueY = []

# one player is always on the center for kicking.
playerBlueX.append(290)
playerBlueY.append(380)

# one player should be in the box.
playerBlueX.append(random.randint(100, 500))
playerBlueY.append(random.randint(100, 140))

# rest blue players (2 players) are randomised.
for i in range(3):
	playerBlueX.append(random.randint(100, 500))
	playerBlueY.append(random.randint(175, 350))


# score calculation
score = 0
score_font = pygame.font.Font('leaves_and_ground.ttf', 45)

def ball(x, y):
	screen.blit(ballImage, (x, y))

def playerRed(x , y, i):
	screen.blit(playerRedImage[i], (x, y))

def playerBlue(x, y, i):
	screen.blit(playerBlueImage[i], (x, y))

def show_score():
	score_text = score_font.render("Score : " + str(score), True, (0, 0, 0))
	screen.blit(score_text, (10, 1))

def red_obstruct():
	warning_text = score_font.render('Warning: Red Player might obstruct the ball path.',True, (0, 0, 0))
	screen.blit(warning_text, (300, 300))


# Goal coordinates..
goalX = 290
goalY = 10
goalImage = pygame.image.load('goal.png')


def showGoal():
	screen.blit(goalImage, (goalX, goalY))


# calculations - backend. 
def distance(x1, y1, x2, y2):
	return math.sqrt(math.pow(x2 - x1, 2) +  math.pow(y2 - y1, 2))

def shortest_path(bx, by, rx, ry):
	# checking for blue.
	# path 1.... 0 - center(1) --> Goal
	# path 2.... 0 - 2 --> Goal
	# path 3.... 0 - 2 --> center(1) --> goal
	# path 4.... 0 - 3 --> Goal
	# path 5.... 0 - 3 --> center(1) --> goal
	
	# calculate distances of all the paths and compare
	path_distances = []

	dist0_1 = distance(bx[0], by[0], bx[1], by[1])
	dist0_2 = distance(bx[0], by[0], bx[2], by[2])
	dist0_3 = distance(bx[0], by[0], bx[3], by[3])
	dist2_goal = distance(bx[2], by[2], goalX, goalY)
	dist3_goal = distance(bx[3], by[3], goalX, goalY)
	dist1_goal = distance(bx[1], by[1], goalX, goalY)
	dist1_2 = distance(bx[1], by[1], bx[2], by[2])
	dist1_3 = distance(bx[1], by[1], bx[3], by[3])

	# path 1 distance.
	path_distances.append(dist0_1 + dist1_goal)
	path_distances.append(dist0_2 + dist2_goal)
	path_distances.append(dist0_2 + dist1_2 + dist1_goal)
	path_distances.append(dist0_3 + dist3_goal)
	path_distances.append(dist0_3 + dist1_3 + dist3_goal)

	ans, index = 10e9 + 7, -1
	for i in range(5):
		if ans > path_distances[i]:
			ans = path_distances[i]
			index = i

	# so the ball has to travel the path - index.
	return index

# finding the shortest path.
path_to_go = shortest_path(playerBlueX, playerBlueY, playerRedX, playerRedY)
print(path_to_go)


# backend.
	# path 1.... 0 - center(1) --> Goal
	# path 2.... 0 - 2 --> Goal
	# path 3.... 0 - 2 --> center(1) --> goal
	# path 4.... 0 - 3 --> Goal
	# path 5.... 0 - 3 --> center(1) --> goal

traverse = {}
traverse[0] = [0, 1]
traverse[1] = [0, 2]
traverse[2] = [0, 2, 1]
traverse[3] = [0, 3]
traverse[4] = [0, 3, 1]
# stored all paths in traverse dictionary.


def line_draw(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	if abs(dx) > abs(dy):
		steps = abs(dx)
	else:
		steps = abs(dy)
	steps = 800
	xinc, yinc = dx / steps, dy / steps
	x,y = x1,y1
	for i in range(steps):
		x += xinc
		y += yinc
		# check for red player.
		for j in range(len(playerRedX)):
			if x == playerRedX[j] and y == playerRedY[j]:
				print("collision with red possible")
				red_obstruct()
		ball(x, y)
		pygame.display.update()



running = True


# at the start, the game is by default paused.
pause = False  


ballX, ballY = playerBlueX[0], playerBlueY[0]



while running:
	screen.fill((0, 0, 0))
	screen.blit(background, (0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.K_p:
			pause = True

	# team red.
	# player in the inner circle = red[0]
	for i in range(3):
		playerRed(playerRedX[i], playerRedY[i], i)
	
	# team blue.
	# Kicker = blue[0]
	# player in the inner circle = blue[1]
	for i in range(4):
		playerBlue(playerBlueX[i], playerBlueY[i], i)


	# if path == 0:
		# check for the first coordinate
		# if ball
	if not pause:
		print('path to go: ', path_to_go)
		if path_to_go >= 0:
			for i in traverse[path_to_go]:
				if ballX == playerBlueX[i] and ballY == playerBlueY[i]:
					continue
				else:
				# ballX, ballY == playerBlueX[i], playerBlueY[i]
					line_draw(ballX, ballY, playerBlueX[i], playerBlueY[i])
					score += math.trunc(distance(ballX, ballY, playerBlueX[i], playerBlueY[i]))
					# show_score()
					ballX, ballY = playerBlueX[i], playerBlueY[i]

			line_draw(ballX, ballY, goalX, goalY)
			ballX, ballY = goalX, goalY
		# break
			pause = True
	show_score()
	showGoal()
	ball(ballX, ballY)
	pygame.display.update()
