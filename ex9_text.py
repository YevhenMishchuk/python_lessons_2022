from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_text(180,100, text='some materials conduct heat better than others')
canvas.create_text(180,130, text='the hardness of a material affects its durability',\
    fill='red')
canvas.create_text(180,160, text='copper is an excellent thermal conductor',\
    fill='green', font=('Times',15))
tk.mainloop()