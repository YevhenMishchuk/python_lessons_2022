from email.mime import image
from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=960, height=600)
canvas.pack()
my_image=PhotoImage(file='/home/marsy/py_for_sci/exercises_29_04_2022/1_Nature_1.png')
canvas.create_image(0,0,anchor=NW, image=my_image)
tk.mainloop()