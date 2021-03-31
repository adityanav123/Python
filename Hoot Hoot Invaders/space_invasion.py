import pygame
import random
import math

from pygame import mixer # for music 

# Initialise pygame.
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600)) # Width X Height.


# setting image background.
background = pygame.image.load('background.jpg')
pause_menu = pygame.image.load('pause_menu.png')

# background sound.
mixer.music.load('background_sound.mp3')
# mixer.music.set_volume(0.1)
mixer.music.set_volume(0.03)
# print(mixer.music.get_volume())
mixer.music.play(-1)

# Title and Icon.
pygame.display.set_caption('Hoot-Hoot Invaders')
icon = pygame.image.load('chick.png')
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load('gunslinger.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

# multiple enemies
for i in range(num_of_enemies):
	enemyImage.append(pygame.image.load('enemy.png'))
	enemyX.append(random.randint(0, 735))
	enemyY.append(random.randint(50, 150))
	enemyX_change.append(0.3)
	enemyY_change.append(40)

# Bullet
bulletImage = pygame.image.load('bullet2.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready" # ready - can't see the bullet on the screen.
# fire -  bullet is currently moving.

# Score
score_value = 0
font = pygame.font.Font('forturn.ttf', 32)
textX = 10
textY = 10


# pause game state.
pause = False

# game over text.
over_font = pygame.font.Font('Hiatus.ttf', 60)

# pause game text.
pause_font = pygame.font.Font('leaves_and_ground.ttf', 60)

# exit game text
exit_font = pygame.font.Font('leaves_and_ground.ttf', 30)


def exit_message():
	exit_text = exit_font.render('Press Q to Exit', True, (0, 0, 0))
	screen.blit(exit_text, (680, 10))

def escape_to_continue_screen():
	pause_text = pause_font.render('Paused! \n Press Escape to continue', True, (0, 0, 0))
	screen.blit(pause_text, (100, 250))

def game_over_text():
	global score_value
	over_text = over_font.render("Game Over! \n Your Score is - " + str(score_value), True, (0, 0, 0)) # RGB
	screen.blit(over_text, (100, 250))

def show_score(x, y):
	score = font.render("Score : " + str(score_value), True, (0, 0, 0)) # RGB
	screen.blit(score, (x, y))

def player(x, y):
	screen.blit(playerImage, (x , y)) # blit - to draw

def enemy(x, y, i):
	screen.blit(enemyImage[i], (x, y))

def fireBullet(x, y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bulletImage, (x + 5, y + 10)) # little bit above the pistol

def isCollision(enemyX, enemyY, bulletX, bulletY):
	distance = math.sqrt((math.pow(enemyX - bulletX ,2)) + (math.pow(enemyY - bulletY, 2)))
	if distance < 27:
		return True
	else:
		return False


# GAME LOOP.
running = True
while running:
	# change background color. RGB values.
	screen.fill((0, 0, 0))
	# background image
	if not pause:
		screen.blit(background, (0, 0))
	if pause:
		screen.blit(pause_menu, (0, 0))
		escape_to_continue_screen()
		exit_message()

	for event in pygame.event.get(): # all events
		if event.type == pygame.QUIT: # check exit button.
			running = False

		# if keystroke is pressed,check right/left
		if event.type == pygame.KEYDOWN: # i.e. key is being pressed.
			if event.key == pygame.K_q and pause:
				exit()
			# print("A keystroke is pressed.")
			if event.key == pygame.K_LEFT: # left arrow.
				if not pause:
					playerX_change = -0.3
				# print("left arrow is pressed")
			if event.key == pygame.K_RIGHT:
				if not pause:
					playerX_change = 0.3
				# print("right arrow is pressed")
			if event.key == pygame.K_SPACE:
				if bullet_state is "ready" and not pause:
					# bullet sound.
					bullet_sound = mixer.Sound("fire.wav")
					bullet_sound.set_volume(0.11)
					bullet_sound.play()
					# get the current x coordinate of the pistol.
					bulletX = playerX
					fireBullet(bulletX, bulletY) # fire a bullet

			# Pause functionality
			if event.key == pygame.K_ESCAPE:
				if pause == False:
					pause = True
				else:
					pause = False # resume the game.

		if event.type == pygame.KEYUP: # key is released.
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				# print("key is released.")
				playerX_change = 0

				
	if not pause:
		playerX += playerX_change

		#setting boundaries of the game.
		if playerX < 0:
			playerX = 0
		elif playerX >= 736:
			playerX = 736

		# enemy movement boundary check.
		for i in range(num_of_enemies):

			# Game Over.
			if enemyY[i] > 440: # 440.
				for j in range(num_of_enemies):
					enemyY[j] = 2000
					game_over_text()
					# exit_message()
				break

			enemyX[i] += enemyX_change[i]
			if enemyX[i] <= 0:
				enemyX_change[i] = 0.25
				enemyY[i] += enemyY_change[i]
			elif enemyX[i] >= 736:
				enemyX_change[i] = -0.25
				enemyY[i] += enemyY_change[i]

			collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
			if collision:
				# enemy dead sound.
				explosion_sound = mixer.Sound("death.wav")
				explosion_sound.play()
				bulletY = 480 # reset the bullet
				bullet_state = "ready" 
				score_value += 1 # enemy hit!
				# print(score_value)
				enemyX[i] = random.randint(0, 735)
				enemyY[i] = random.randint(0, 150)
			# printing the enemy
			enemy(enemyX[i], enemyY[i], i)

		# bullet movement
		if bulletY <= 0:
			bulletY = 480
			bullet_state = 'ready'
		if bullet_state is "fire":
			fireBullet(bulletX, bulletY)
			bulletY-=bulletY_change

		# collision
		

		player(playerX, playerY) # show the player on screen.
	show_score(textX, textY)


	pygame.display.update() # update the game screen.



