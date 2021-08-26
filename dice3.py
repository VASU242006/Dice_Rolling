from tkinter import *
from PIL import Image, ImageTk
import random
root = Tk()
# root.geometry("1000x700")
root.minsize(600,600)
root.maxsize(600,600)
dices = ['die1.png', 'die2.png','die3.png','die4.png','die5.png','die6.png']

img = ImageTk.PhotoImage(Image.open(random.choice(dices)))


label1 = Label(root, image=img)
label1.image = img
# label1.configure(image=img)



def dice_rolled():
    img = ImageTk.PhotoImage(Image.open(random.choice(dices)))
    print(img)  
    label1.configure(image=img)
    label1.image = img
    label1.pack()

btn = Button(root,text="Click To Roll the Dice",bg="black",fg="white",font=("Roman",30), command=dice_rolled)
btn.pack(side=BOTTOM)
label1.pack()
root.mainloop()