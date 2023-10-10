class TodoList:
    def __init__(self):
        self.list={}
    def addTodo(self,task):
        self.list[task]=False
    def finishTask(self,task):
        self.list[task]=True
