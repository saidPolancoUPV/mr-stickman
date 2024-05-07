from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        
    def draw(self, speed=3):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        print(f"id: {self.id} pos: {pos}")
        if pos[1] <= 0:
            self.y = speed
        if pos[3] >= self.canvas_height:
            self.y = -speed
        if pos[0] <= 0:
            self.x = speed
        if pos[2] >= self.canvas_width:
            self.x = -speed


tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

ball = Ball(canvas, "red")
#ballb = Ball(canvas, "blue")
#ballg = Ball(canvas, "green")

while 1:
    ball.draw(1)
    #ballb.draw(3)
    #ballg.draw(5)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
