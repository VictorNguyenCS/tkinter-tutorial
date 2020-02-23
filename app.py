#https://likegeeks.com/python-gui-examples-tkinter-tutorial/

from tkinter import *

window = Tk()
window.geometry('350x200')
window.title("Welcome to Victors App")

#Normal Text
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

#Input box
txt = Entry(window,width=10)
txt.grid(column=1, row=0)

#Buttton
def clicked():
    res = "I want " + txt.get()
    lbl.configure(text= res)

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

#Check-Box
chk_state = BooleanVar()
chk_state.set(0) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=1)

#Combo-Box
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=2)

window.mainloop()

