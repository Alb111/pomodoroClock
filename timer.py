import time
import datetime
import tkinter
import customtkinter

class Pomodoro:
    
    def __init__(self, root):
        self.studyTime = 0
        self.breakTime = 0
        self.studyTrue = True
        self.repeats = 0
        self.root = root
        self.label = customtkinter.CTkLabel(root, text="")
        self.label.pack()
    
    def setStudyTime(self, x):
        self.studyTime = x
    
    def getStudyTime(self):
        return self.studyTime
    
    def setBreakTime(self, x):
        self.breakTime = x
    
    def getBreakTime(self):
        return self.breakTime
    
    def setStudyTrue(self, x):
        self.studyTrue = x
    
    def getStudyTrue(self):
        return self.studyTrue
    
    def setRepeats(self, x):
        self.repeats = x
    
    def getRepeats(self):
        return self.repeats
    
    def stopwatch(self, total_seconds):
        while total_seconds > 0:
            timer = datetime.timedelta(seconds=total_seconds)
            self.label.configure(text=timer)
            self.root.update()
            time.sleep(1)
            total_seconds -= 1
    
    def start(self):
        while self.repeats > 0:
            if self.studyTrue:
                self.stopwatch(self.studyTime * 60)
                self.studyTrue = False
            else:
                self.stopwatch(self.breakTime * 60)
                self.studyTrue = True
            self.repeats -= 1




        



    

    
    
    

        


