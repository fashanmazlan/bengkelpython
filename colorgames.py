# import the modules 
import tkinter
import random

# Senaraikan kemungkinan warna.
colours = ['Red','Blue','Green','Pink','Black',
		'Yellow','Orange','White','Purple','Brown']
score = 0

# Masa yang diperuntukkan.
timeleft = 30

# Fungsi untuk memulakan permainan.
def startGame(event):
	
	if timeleft == 30:
		
		# Memulakan kira detik.
		countdown()
		
	# larian fungsi untuk pilih warna yang serusnya.
	nextColour()

# Fungsi untuk memilih dan memaparkan warna seterusnya.
def nextColour():

	# use the globally declared 'score'
	# and 'play' variables above.
	global score
	global timeleft

	# if a game is currently in play
	if timeleft > 0:

		# make the text entry box active.
		e.focus_set()

		# Jika warna yang ditaip adalah sama 
		# kepada warna pada teks
		if e.get().lower() == colours[1].lower():
			
			score += 1

		# Kosongkan kotak masukkan teks. 
		e.delete(0, tkinter.END)
		
		random.shuffle(colours)
		
		# change the colour to type, by changing the 
		# text _and_ the colour to a random colour value
		label.config(fg = str(colours[1]), text = str(colours[0]))
		
		# update the score.
		scoreLabel.config(text = "Score: " + str(score))


# Fungsi pemasa undur
def countdown():

	global timeleft

	# jika permainan sedang dimainkan.
	if timeleft > 0:

		# Kurungkan pemasa.
		timeleft -= 1
		
		# kemaskini label masa yang tinggal
		timeLabel.config(text = "Time left: "
							+ str(timeleft))
								
		# Jalankan fungsi semula selepas 1 saat.
		timeLabel.after(1000, countdown)


# Driver Code

# menghasilkan tetingkap GUI 
root = tkinter.Tk()

# set the title
root.title("COLORGAME")

# set the size
root.geometry("375x200")

# add an instructions label
instructions = tkinter.Label(root, text = "Type in the colour "
						"of the words, and not the word text!",
									font = ('Helvetica', 12))
instructions.pack() 

# add a score label
scoreLabel = tkinter.Label(root, text = "Press enter to start",
									font = ('Helvetica', 12))
scoreLabel.pack()

# add a time left label
timeLabel = tkinter.Label(root, text = "Time left: " +
			str(timeleft), font = ('Helvetica', 12))
			
timeLabel.pack()

# add a label for displaying the colours
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()

# add a text entry box for
# typing in colours
e = tkinter.Entry(root)

# run the 'startGame' function 
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()

# start the GUI
root.mainloop()
