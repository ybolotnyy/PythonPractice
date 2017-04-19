from Tkinter import *

win = Tk()
f = Frame(win)

b1 = Button(f, text = "One")
b2 = Button(f, text = "Two")
b3 = Button(f, text = "Three")

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)

l = Label(win, text="This is a label")

# l.grid(row=0,column=0)
# f.grid(row=1,column=0)

l.pack()
f.pack()


win.mainloop()