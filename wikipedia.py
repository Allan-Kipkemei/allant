from tkinter import *
import wikipedia

root = Tk()
root.title("Wiki")
root.geometry("1000x1000")

frame = Frame(root)
input = Entry(frame, width = 50)
input.pack()
result = 'j'


def search():
     global result
     result = input.get()
     summary = wikipedia.summary(result, sentences=3)
     text.insert('1.0',summary)
text = Text(root, font = ('ariel',20))

button = Button(frame, text = 'Search', command = search)                                                 
button.pack(side = RIGHT)
frame.pack(side = TOP)
text.pack()
root.mainloop()