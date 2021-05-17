from matplotlib import *
from PIL import Image, ImageDraw, ImageFont
import PIL
from random import SystemRandom
import patterns
import os



width, height = None, None

def generateMessageImage(message):
	image = Image.new('RGB', (600, 500), color = (0, 0, 0))
	draw = ImageDraw.Draw(image)

	font = ImageFont.truetype ('hometown.ttf', 60)

	draw.text ((75, 100), message, font = font, fill = (255, 255, 255) )
	
	image.save('./test-images/' + message + '.png', 'PNG')

def showOriginal(img):
	img.show()

def encrypt(img):
	global width, height
	width = img.size[0]
	height = img.size[1]
	img = img.resize((width, height))

	binary_img = img.convert('1')

	binary_image = binary_img.resize((width, height))

	binary_img = binary_img.convert('1')

	image1 = Image.new('1', (width, height))
	image2 = Image.new('1', (width, height))
	image3 = Image.new('1', (width, height))
	image4 = Image.new('1', (width, height))
	# print("size of original image : ",binary_img.size[1], binary_img.size[0])

	draw1 = ImageDraw.Draw(image1)
	draw2 = ImageDraw.Draw(image2)
	draw3 = ImageDraw.Draw(image3)
	draw4 = ImageDraw.Draw(image4)


	for i in range(width):
		for j in range(height):
			pixel = binary_img.getpixel((i, j)) # traversing through each pixel.
			if pixel == 255:
				pixel = 1
		
			if pixel == 1:
				state = patterns.white_pattern_generate()
				draw1.point((i, j), state[0])
				draw2.point((i, j), state[1])
				draw3.point((i, j), state[2])
				draw4.point((i, j), state[3])

			else:
				state = patterns.black_pattern_generate()
				draw1.point((i, j), state[0])
				draw2.point((i, j), state[1])
				draw3.point((i, j), state[2])
				draw4.point((i, j), state[3])

	
	# Saving the shares.
	image1.save('./Shares/Share-1.png', 'PNG')
	image2.save('./Shares/Share-2.png', 'PNG')
	image3.save('./Shares/Share-3.png', 'PNG')
	image4.save('./Shares/Share-4.png', 'PNG')
	return (image1, image2, image3, image4)

def decrypt(image1, image2, image3, image4):
	image_out = Image.new('1', (width, height))
	draw_out = ImageDraw.Draw(image_out)

	for i in range(width):
		for j in range(height):
			pixel1 = image1.getpixel((i, j))
			pixel2 = image2.getpixel((i, j))
			pixel3 = image3.getpixel((i, j))
			pixel4 = image4.getpixel((i, j))
												
			temp = pixel1 ^ pixel2
			temp ^= pixel3
			temp ^= pixel4
			draw_out.point((i, j), temp)
	image_out.save('./Shares/Reconstructed-Image.png', 'PNG')
	return image_out





# MAIN.
# img = Image.open('./test-images/aditya_original.png')

# (i1, i2, i3, i4) = encrypt(img)	
# decrypt(i1, i2, i3, i4)

# showOriginal(img)















