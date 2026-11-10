from user import User
from task import Task
from priority_task import PriorityTask
from task_queue import TaskQueue


def main():
    '''Entry point, create objects and run the application'''
    # Create a user
    user1 = User(1, "alex", "alex@example.com")

    # Passing user object as 'A Task is assigned to a User object'
    # Create a normal task
    task1 = Task(
        101,
        "Build login page",
        "Create the login functionality",
        user1
    )

    # Create 2 priority tasks
    task2 = PriorityTask(
        102,
        "Fix login bug",
        "Resolve the login authentication issue",
        1,
        user1
    )
    task3 = PriorityTask(
        103,
        "Update dashboard",
        "Improve dashboard performance",
        3,
        user1
    )

    # Display task information
    # print(task1)
    # print(task2)
    # print(task3)

    # To check the value of user assigned email address
    # print("Task 1 Assigned to:", task1.assigned_to.get_email())
    
    # Create a task queue
    task_queue = TaskQueue()

    # Add tasks to the queue
    task_queue.add_task(task1)
    task_queue.add_task(task2)
    task_queue.add_task(task3)

    # Display all tasks
    task_queue.display_tasks()
        
    # Search tasks
    results = task_queue.search_tasks("login")
    
    print("\n ----- Search results for login keyword: ------")
    for task in results:
        print(task)

    # Get the next task to work on
    print("\n ----- Next task to work on: -----")
    print(task_queue.get_next_task())


if __name__ == "__main__":
    main()