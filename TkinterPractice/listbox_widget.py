from Tkinter import *

def but1():
    print("Button was pushed")
    b1.configure(text="You just toched me )")


win = Tk()

lb = Listbox(win, height=3)

lb.insert(END,"first entry")
lb.insert(END,"second entry")
lb.insert(END,"third entry")
lb.insert(END,"forth entry")
#lb.insert(TOP,"zero entry")

sb = Scrollbar(win,orient=VERTICAL)

sb.pack(side=RIGHT,fill=Y)
lb.pack()

sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)

print(lb.curselection())

win.mainloop()

