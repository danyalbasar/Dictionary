from tkinter import *
from PIL import Image, ImageTk
import json
from difflib import get_close_matches

data_load = json.load(open("data.json"))

def search_word(word):
	if word in data_load:
		meaning_word.delete(1.0, END)
		meaning_word.config(fg="red")
		meaning_word.insert(END, data_load[word])
	elif len(get_close_matches(word, data_load.keys())) > 0:
		meaning_word.config(fg="red")
		meaning_word.delete(1.0, END)
		meaning_word.insert(END, "Were you finding {}? If yes then it's meaning is: {} ".format(get_close_matches(word, data_load.keys())[0],	
				data_load[get_close_matches(word, data_load.keys())[0]]))
		final = get_close_matches(word, data_load.keys())
root = Tk()
root.title("MY OWN DICTIONARY")

image = Image.open("dict.png")
image_picture = ImageTk.PhotoImage(image)
dest_pic = Label(root, image=image_picture)
dest_pic.pack()

a = StringVar()
word_meaning = Entry(root, textvariable=a, bg="black", insertbackground="red", fg="red", font=("arial", 40, "bold"))
word_meaning.place(relx=.185, rely=.70, relwidth=.63, relheight=.082)

button_1 = Button(root, text="SEARCH THE WORD", command=lambda:search_word(a.get()), bg="red", fg="white", font=("arial", 40, "bold"))
button_1.place(relx=.25, rely=.85, relwidth=.50, relheight=.052)

meaning_word = Text(root, bg="black", font=("arial", 25, "bold"))
meaning_word.place(relx=.100, rely=.05, relwidth=.80, relheight=.16)


root.mainloop()