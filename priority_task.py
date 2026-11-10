from task import Task

class PriorityTask(Task):
    '''Extend Task with priority'''
    def __init__(self, task_id, title, description, priority, assigned_to=None):
        super().__init__(task_id, title, description, assigned_to)
        self.priority = priority    # 1 = high, 2 = medium, 3 = low
 
    def __repr__(self):
        return f'PriorityTask(Title = {self.title}, Priority = {self.priority}, Status = {self.status} )'