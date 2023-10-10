import time
import datetime
class Pondomoro:
    
    def __init__(self):
        self.studyTime=0
        self.breakTime=0
        self.studyTrue=True
        self.repeats=0
    
    def setStudyTime(self,x):
        self.studyTime=x
    
    def getStudyTime(self):
        return self.studyTime
    
    def setBreakTime(self,x):
        self.breakTime=x
    
    def getBreakTime(self):
        return self.breakTime
    
    def setStudyTrue(self,x):
        self.studyTrue=x
    
    def getStudyTrue(self):
        return self.studyTrue
    
    def setRepeats(self,x):
        self.repeats=x
    
    def getRepeats(self):
        return self.repeats
    
    def stopwatch(self, total_seconds):
        
        while(total_seconds!=0):
            timer=datetime.timedelta(seconds = total_seconds)
            print(timer, end="\r")
            time.sleep(1)
            total_seconds -= 1
    
    def start(self):
        while(self.repeats>0):
            if(self.studyTrue):
                self.stopwatch(self.studyTime * 60 )
                self.studyTrue=False
            else:
                self.stopwatch(total_seconds = self.breakTime * 60)
                self.studyTrue=False
            self.repeats=self.repeats-1

x=Pondomoro()
x.setBreakTime(.5)
x.setStudyTime(.25)
x.setRepeats(2)
x.start()

        
        



        



    

    
    
    

        

