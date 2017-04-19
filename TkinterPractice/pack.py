from Tkinter import *

win = Tk()

b1 = Button(win, text = "One")
b2 = Button(win, text = "Two")

b1.pack(side=LEFT)
b2.pack(side=RIGHT)

win.mainloop()