import customtkinter
import tkinter as tk

class RoundButton():
   def __init__(self, canvas, command, radius: int = 200, x: int = 450, y: int = 300, fill: str = "red"):
      self.canvas = canvas
      self.fill = fill
      self.command = command
      x1, x2, y1, y2 = x - radius, x + radius, y - radius, y + radius
      print(x, y)
      print(x1, x2, y1, y2)

      self.button = canvas.create_oval(x1, y1, x2, y2, fill=self.fill)
      self.canvas.tag_bind(self.button, '<Button-1>', self.command)

   def update(self, radius: int, x: int, y: int):
      self.radius, self.x, self.y = radius, x, y
      x1, x2, y1, y2 = self.x - self.radius, self.x + self.radius, self.y - self.radius, self.y + self.radius
      self.canvas.coords(self.button, x1, y1, x2, y2)
   
   

