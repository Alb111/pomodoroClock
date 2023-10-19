import tkinter
import customtkinter

def update_label():
    global x
    if x > -1:
        
        label.configure(text=x)
        x -= 1
        root.after(1000, update_label)  # Schedule the function to run again after 1000 ms (1 second)

root = customtkinter.CTk()
root.title('gui prac')
root.geometry("500x500")
x = 5
label = customtkinter.CTkLabel(root, text=x)
label.pack()

update_label()  # Start the label update function

root.mainloop()
