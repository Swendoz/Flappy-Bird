import tkinter as tk
from tkinter import *

import configs
import main

window = tk.Tk()

window.title("Flappy Bird")
window.geometry("288x512")
window.resizable(False, False)

photo = PhotoImage(file = 'assets/sprites/bird-midflap.png')
window.wm_iconphoto(False, photo)

bgImage = PhotoImage(file="assets/sprites/background.png")
bgLabel = Label(window, image=bgImage)
bgLabel.place(x=0, y=0)


def my_click():
   configs.GRAVITY = float(name.get())
   main.play_game()
   # print(name.get())


name = Entry(window, width=50)
name.pack(padx=10, pady=10)

button = Button(window, text="Submit", command=my_click)
button.pack(pady=10)

window.mainloop()
