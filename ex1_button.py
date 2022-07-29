def Hallo():
    print("Hallo, wie geht es Ihnen?")

def menschlich(breite=50, höhe=180):
    print("Mine brite %s cm, mine höhe %s cm" % (breite,höhe))


from tkinter import *
tk=Tk()
btn=Button(tk, text="klick mich", command=menschlich)
btn.pack()

tk.mainloop()