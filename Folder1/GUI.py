## GUI for user to enter STUDY_TIME, REST_TIME , and NUM_OF_CYCLES

import tkinter
import customtkinter
from main import Pomodoro

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root=customtkinter.CTk()
root.title('gui prac')
root.geometry("500x500")

def open_new_window():
    new_window = customtkinter.Toplevel(root)
    new_window.title("New Window")
    

def submit():
    StudyTime = int(myEntry.get())
    RestTime = int(myEntry1.get())
    Cycle = int(myEntry2.get())

    x = Pomodoro(root)
    x.setStudyTime(StudyTime)
    x.setBreakTime(RestTime)
    x.setRepeats(Cycle)
    x.start()
    
    
    
    
myLabel= customtkinter.CTkLabel(root, text='Pondomoro', font=("Comfortaa", 50), text_color="blue")
myLabel.pack(pady=5)
myLabel= customtkinter.CTkLabel(root, text='Timer', font=("Comfortaa", 50), text_color="blue")
myLabel.pack(pady=5)
myEntry=customtkinter.CTkEntry(root, placeholder_text="Enter Study Time", width=400)
myEntry.pack(pady=20)
myEntry1=customtkinter.CTkEntry(root, placeholder_text="Enter Rest Time", width=400)
myEntry1.pack(pady=20)
myEntry2=customtkinter.CTkEntry(root, placeholder_text="Enter Number of Cycles", width=400)
myEntry2.pack(pady=20)

myButton= customtkinter.CTkButton(root, text="Submit", command=submit, fg_color=("gray", "blue"))
myButton.pack(pady=20)




root.mainloop()