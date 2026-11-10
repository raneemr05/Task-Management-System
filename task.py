class Task:
    '''Define common task attributes and behaviour'''
    def __init__(self, task_id, title, description, assigned_to= None):
        # task_id is an internal identifier that nothing external should modify
        self.__task_id = task_id   # private - accessed via getter
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.status = 'pending'
        self.priority = 2 # default priority is medium
        
    def get_task_id(self):
        return self.__task_id
    
    def complete(self):
        self.status = 'complete'
        
    # __repr__ provide a useful representation of an object, often for debugging
    def __repr__(self):
        return f"Task (Title = {self.title}, Priority = {self.priority}, Status = {self.status} )"
    
    # OR 
    #  __str__() is intended for a more user-friendly display
    
    # OR if you don't want to use special methods you can create your custome display method
    # def display_details(self):
    # print(f"Task: {self.title}")
    # print(f"Status: {self.status}")