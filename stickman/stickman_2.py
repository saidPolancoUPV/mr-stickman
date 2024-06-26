from tkinter import *
import random
import time


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Mr. Stick Man Races for the Exit")
        self.tk.resizable(False, False)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        ######################## NEW ###########################################
        self.bg = PhotoImage(file="./imgs/background.gif")
        w = self.bg.width()
        h = self.bg.height()
        
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * w, y * h,
                                         image=self.bg, anchor='nw')
        self.sprites = []
        self.running = True
        ########################################################################