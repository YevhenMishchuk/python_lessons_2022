from tkinter import *
import random
tk=Tk()
canvas=Canvas(tk, width=400, height=400)
canvas.pack()

def random_polygon(A, B, fill_color):
    x1=random.randrange(A)
    x2=random.randrange(B)
    x3=x1+random.randrange(A)
    x4=x2+random.randrange(B)
    x5=x2+random.randrange(A)
    x6=x1+random.randrange(B)
    canvas.create_polygon(x1,x2,x3,x4,x5,x6, fill = fill_color)

#for x in range (0,50):
#   random_polygon(400,400)
    

random_polygon(400,400, 'green')
random_polygon(400,400, 'red')
random_polygon(400,400, 'blue')
random_polygon(400,400, 'orange')
random_polygon(400,400, 'yellow')
random_polygon(400,400, 'pink')
random_polygon(400,400, 'purple')

tk.mainloop()