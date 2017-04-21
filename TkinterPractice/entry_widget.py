from Tkinter import *

def but1():
    print("Button was pushed")
    b1.configure(text="You just toched me )")


win = Tk()
f = Frame(win)

l = Label(win, text="This is a label")

v = StringVar()
e = Entry(win,textvariable=v)

l.pack()
e.pack()

v.set("hello")
print(v.get())

win.mainloop()

