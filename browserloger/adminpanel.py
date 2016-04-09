from tkinter import *


apencere = Tk()


apencere.title(u"Browser Logger/Admin panel")
apencere.geometry("300x150+100+100")

karsilama = Label(apencere)
karsilama.config(text = u"\n\nAdmin panel vizelerden sonra yapılacaktır.")
karsilama.pack()


mainloop ()