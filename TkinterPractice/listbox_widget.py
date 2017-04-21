from Tkinter import *

def but1():
    print("Button was pushed")
    b1.configure(text="You just toched me )")


win = Tk()

lb = Listbox(win, height=3)
lb.pack()
lb.insert(END,"first entry")
lb.insert(END,"second entry")
lb.insert(END,"third entry")
#lb.insert(TOP,"zero entry")

win.mainloop()

