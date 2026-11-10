# Task Management System

A simple Python task management system demonstrating object-oriented programming, data structures, searching techniques and time complexity.

## Project Overview

The system manages tasks, assigned users and task priorities. It allows tasks to be added to a queue, displayed in priority order and searched by keyword.

### Project Structure

```text
task_management/
├── task.py
├── priority_task.py
├── user.py
├── task_queue.py
└── main.py
```


## 1. Concepts Covered

| Concept | Where it is demonstrated |
|---|---|
| Classes and objects | `Task`, `PriorityTask`, `User` and `TaskQueue` |
| Constructors | `__init__()` initialises object attributes |
| Encapsulation | Private attributes such as `__task_id` and `__email`, accessed through getter methods |
| Inheritance | `PriorityTask` inherits from `Task` |
| Method overriding | `PriorityTask` provides its own implementation of `__repr__()` |
| Polymorphism | Printing a `Task` or `PriorityTask` object calls the appropriate `__repr__()` implementation |
| Association | A `Task` has an assigned `User` object through its `assigned_to` attribute |
| Lists | `TaskQueue` uses a list to store task objects |
| Sorting | Tasks are sorted according to their priority |
| Linear search | `search_tasks()` checks task titles and descriptions for a keyword |

### Inheritance vs Association/Composition

These relationships represent different concepts:

- **Inheritance (is-a):** A `PriorityTask` is a type of `Task`.
- **Composition (has-a relationship):** A `Task` is assigned to a `User` object.


## 2. SOLID Principles

Three relevant SOLID principles demonstrated in this example:

| Principle | How it is demonstrated |
|---|---|
| **SRP – Single Responsibility Principle** | `User` manages user information, `Task` manages task information, `PriorityTask` extends task functionality with priority, and `TaskQueue` manages the collection of tasks. |
| **OCP – Open/Closed Principle** | New specialised task types can be introduced by extending `Task`, without modifying the existing base class. |
| **LSP – Liskov Substitution Principle** | A `PriorityTask` can be used wherever a `Task` is expected because it inherits the common attributes and behaviour of `Task`. |


## 3. Time Complexity (Big-O)

Big-O notation describes how the time taken by an operation grows as the amount of data increases.

Let `n` represent the number of tasks in the queue.

### Complexity of the Current Implementation

| Method | Time Complexity | Explanation |
|---|---|---|
| `add_task()` | O(n log n) | A task is appended and the list is sorted after every insertion. Sorting dominates the operation. |
| `get_next_task()` | O(n) | `pop(0)` removes the first item, requiring the remaining list elements to shift. |
| `is_empty()` | O(1) | Checks whether the list is empty. |
| `search_tasks()` | O(n) | Checks each task's title and description for the keyword. |
| `display_tasks()` | O(n) | Iterates through the tasks and displays each one. |

*Note: Search complexity is simplified to O(n), assuming reasonably bounded title and description lengths. Actual string comparisons also depend on the amount of text being searched.*

## 4. Improving Search Complexity

The current `search_tasks()` method uses **linear search**.

```python
def search_tasks(self, keyword):
    keyword = keyword.lower()

    return [
        task for task in self._tasks
        if keyword in task.title.lower()
        or keyword in task.description.lower()
    ]
```

For every search, the method checks each task individually.

As the number of tasks grows, the search may take longer.


### Can We Improve This?

One approach is to use a **hash table**, implemented in Python using a dictionary.

Instead of scanning every task during each search, we can build a dictionary that maps individual words to the tasks containing them.

### Example: Building a Word-to-Tasks Dictionary

```python
# Build a word-to-tasks dictionary
word_map = {}

for task in tasks:
    words = set(
        (task.title + " " + task.description).lower().split()
    )

    for word in words:
        if word not in word_map:
            word_map[word] = []

        word_map[word].append(task)


# Search using the dictionary
def search_fast(keyword):
    return word_map.get(keyword.lower(), [])
```

### How Does This Improve Search?

For example, the dictionary might contain:

```python
{
    "login": [task1, task2],
    "dashboard": [task3],
    "authentication": [task2]
}
```

When searching for `"login"`, the dictionary can retrieve the matching tasks directly rather than checking every task.

| Approach | Average Lookup Complexity |
|---|---|
| Linear search through a list | O(n) |
| Dictionary lookup | O(1) |

Dictionary lookup is O(1) on average because Python dictionaries use hashing to locate keys.

### Important Considerations

- The dictionary needs to be built before searching. Building it requires processing the words in the task titles and descriptions.
- The dictionary must be updated whenever tasks are added, removed or modified.
- This example supports exact word matching. It does not provide the same partial-word matching as the original linear search. For example, searching for `"log"` would not find `"login"`.
- `defaultdict(list)` from Python's `collections` module can simplify the process of creating dictionary entries.

## 5. Conclusion

For a small task management system, linear search is a perfectly reasonable choice.

It is straightforward to implement, easy to maintain and performs well when the number of tasks is relatively small.

The dictionary-based approach becomes more useful when the number of tasks grows and keyword searches happen frequently.

The important consideration is not always to choose the approach with the lowest Big-O complexity, but to choose an approach that is appropriate for the size of the data and the requirements of the application.
