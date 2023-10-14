import customtkinter
import tkinter as tk
from RoundButton import RoundButton

app = customtkinter.CTk()
app.title("Pomodoro App")


# Handle button click event here
def on_mainButton_click():
    print("Round button clicked!")

# Create a Canvas widget to draw the round button
canvas = tk.Canvas(app, width=900, height=600, highlightthickness=0)
canvas.pack()

# secondary button
def sec_handleClick(event):
    print("Time to reset!")

## Draw button on the canvas
secButton = RoundButton(canvas, sec_handleClick, radius=70, x=750, y=300, fill="blue")

# main button
def main_handleClick(event):
    print("Timer starts now!")

## Draw button on the canvas
mainButton = RoundButton(canvas, main_handleClick, radius=200, x=450, y=300, fill="red")


def resize(event):
    win_width = canvas.winfo_width()
    win_height = canvas.winfo_height()
    
    print("width:", win_width)
    print("height:", win_height)

    # update button size and position
    new_radius = min(win_width, win_height) // 4
    new_x = win_width // 2
    new_y = win_height // 2
    mainButton.update(radius=new_radius, x=new_x, y=new_y)

    new_radius = min(win_width, win_height) // 6
    new_x = 5 * win_width // 6
    new_y = win_height // 2
    secButton.update(radius=new_radius, x=new_x, y=new_y)

app.bind("<Configure>", resize)

app.mainloop()

