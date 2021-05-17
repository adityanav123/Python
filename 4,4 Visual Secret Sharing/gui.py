import tkinter
from tkinter import *
from tkinter import filedialog
import PIL
import vss_kn
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



fileName = ""
Original_image = None

s1, s2, s3, s4 = None, None, None, None



def encrptClick():
	global Original_image, s1, s2, s3, s4
	path = "./test-images/" + fileName
	img = PIL.Image.open(path)
	Original_image = img
	(s1, s2, s3, s4) = vss_kn.encrypt(img)

	fileLabel = Label(top, text = "Encrypted!", font = ("Fronzy Free Trial", 16)).place(x = 450, y = 190)



	btn.configure(fg = 'black')
	# Displaying the Images.
	fig = plt.figure()
	row, col = 2, 2
	fig.add_subplot(row, col, 1)
	plt.imshow(s1)
	plt.axis('off')
	plt.title('Share - 1')
	fig.add_subplot(row, col, 2)
	plt.imshow(s2)
	plt.axis('off')
	plt.title('Share - 2')

	fig.add_subplot(row, col, 3)
	plt.imshow(s3)
	plt.axis('off')
	plt.title('Share - 3')

	fig.add_subplot(row, col, 4)
	plt.imshow(s4)
	plt.axis('off')
	plt.title('Share - 4')

	plt.show()

	


def fileSelect():
	# pass
	global fileName
	file_path = filedialog.askopenfilename() # to select the file.
	i = -1
	while True:
		if file_path[i] != '/':
			fileName += file_path[i]
		else:
			break
		i -= 1
	fileName = fileName[::-1]
	fileLabel = Label(top, text = "File Selected - " + fileName, font = ("Fronzy Free Trial", 16)).place(x = 100, y = 190)

def decryptClick():
	output = vss_kn.decrypt(s1, s2, s3, s4)
	btn2.configure(fg = 'black')
	output.show()

	fileLabel = Label(top, text = "Decrypted!", font = ("Fronzy Free Trial", 16)).place(x = 600, y = 190)

def showClick():
	vss_kn.showOriginal(Original_image)

def generate():
	message = "" + txt.get()
	print(message)
	vss_kn.generateMessageImage(message)


top = tkinter.Tk()
top.title(" - (4, 4) Visual Secret Sharing - ")
top.geometry('910x600')

windowLogo = PhotoImage(file = 'logo.jpg')
top.iconphoto(False,windowLogo)




ecomplete = PhotoImage(file = 'encrypt-complete.png')
ecomplete = ecomplete.subsample(13, 13)


label = Label(top, text = " - Visual Secret Sharing -", font=("Quantine Personal Use", 45)).place(x = 20, y = 50)



encryptnow = PhotoImage(file = 'encrypt.png')
encryptnow = encryptnow.subsample(13, 13)
btn = Button(top, text = ' Encrypt ',image = encryptnow, compound = LEFT, font = ('Book Antiqua', 17), fg = 'green', command = encrptClick)
btn.place(x = 200, y = 300)
 # image = photoimage

photo = PhotoImage(file = 'file.png')
photoimage = photo.subsample(18, 18)
btn1 = Button(top, text = 'Select File', image = photoimage, compound = LEFT, font = ('Book Antiqua', 17), command = fileSelect)
btn1.place(x = 30, y = 300)


decryptLogo = PhotoImage(file = 'decrypt.png')
decryptLogo = decryptLogo.subsample(10, 10)
btn2 = Button(top, text = 'Decrypt',image = decryptLogo, compound = LEFT, font = ('Book Antiqua', 17), fg = 'green', command = decryptClick)
btn2.place(x = 750, y = 300)

imageLogo = PhotoImage(file = 'image.png')
imageLogo = imageLogo.subsample(30, 30)
btn3 = Button(top, text = 'Show Original Image', image = imageLogo, compound = LEFT, font = ('Book Antiqua', 17), command = showClick)
btn3.place(x = 450, y = 300)


writeLogo = PhotoImage(file = 'pen.jpg')
writeLogo = writeLogo.subsample(11, 11)
btn4 = Label(top, text = 'Custom Message',image = writeLogo, compound = LEFT, font = ('Book Antiqua', 17))
btn4.place(x = 350, y = 400)

txt = Entry(top, width = 50, selectborderwidth = 5, bd = 3, font = ('Book Antiqua', 12))
txt.focus()
txt.place(x = 250, y = 450)

btn5 = Button(top,text = 'Generate', font = ('Book Antiqua', 11), command = generate)
btn5.place(x = 420, y = 490)


top.mainloop()




