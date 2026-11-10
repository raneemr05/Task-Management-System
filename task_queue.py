# Build a task queue using a list

class TaskQueue:
    '''Manages a collection of tasks in priority order.'''
    
    def __init__(self):
        """Initialise an empty task queue."""
        self._tasks = []
        
    def add_task(self,task):
        """
        Add a task to the queue and sort by priority.

        Priority 1 = High, 2 = Medium, 3 = Low.
        """
        self._tasks.append(task)
        # Sort tasks so the highest-priority task comes first.
        # key parameter tells Python which value it should use when comparing items during sorting.
        # Lambda is useful when we need a small function for a specific purpose and 
        # don't want to define a separate named function for it.
        # e.g. def get_priority(t):
        # return t.priority
        self._tasks.sort(key=lambda t: t.priority)
        
    # Retrieve the highest-priority task (from sorted queue) 
    # that needs to be worked on next (means to remove the task from the queue)
    # Note that we are not marking it as complete its just got removed from the queue
    def get_next_task(self):
        """
        Return and remove the highest-priority task.

        Return None if the queue is empty.
        """
        if self._tasks:
            return self._tasks.pop(0)
        return None
    
    def is_empty(self):
        """Return True if the queue contains no tasks."""
        return len(self._tasks) == 0
    
    def display_tasks(self):
        """Display all tasks in priority order."""
        if self.is_empty():
            print("The task queue is empty.")
            return

        print("\nTasks in the queue:")

        for task in self._tasks:
            print(task)
        
    # Time complexity: O(n) Check every task
    def search_tasks(self, keyword):
        """
        Using linear search -> Search task titles and descriptions for a keyword.

        The search is case-insensitive and supports partial matches.
        Returns a list of matching task objects.
        """
        keyword = keyword.lower()
        # A list comprehension using lower method and in operator for substring matching
        # checking each task's title and description to see whether the keyword exists
        return [
            task for task in self._tasks
            if keyword in task.title.lower()
            or keyword in task.description.lower()
        ]
        
        # Method 2 
        # matching_tasks = []
        # for task in tasks:
        #     if (keyword in task.title.lower()
        #             or keyword in task.description.lower()):
        #         matching_tasks.append(task)

        # return matching_tasks