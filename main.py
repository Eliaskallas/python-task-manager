# task class to represent each task
class task:
    def __init__(self, title, duration, priority):
        self.title = title
        self.duration = duration
        self.priority = priority

    def __str__(self):
        return "[" + self.title + " | " + str(self.duration) + " mins | Priority " + str(self.priority) + "]"

# Queue class using a list with custom functions
class TaskQueue:
    def __init__(self):
        self.queue = []

    def insert(self, task):
        self.queue.append(task)

    def extract(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def get_all_tasks(self):
        return self.queue

# Function "complete_next_task" to complete the next task (highest priority)
def complete_next_task(queue):
    if queue.is_empty():
        print("No tasks to complete.")
        return

    # Find task with highest priority (lowest value)
    highest_priority_task = queue.queue[0]
    for task in queue.queue:
        if task.priority < highest_priority_task.priority:
            highest_priority_task = task
    queue.queue.remove(highest_priority_task)
    print("Completed task: " + str(highest_priority_task))


# Function "search_for_task" is a binary search function that operates on a queue sorted by task's title
def search_for_task(queue, title):
    # Step 1: Sort the queue manually using binary insertion sort (case-insensitive by title)
    tasks = queue.queue
    sorted_tasks = []
    for task in tasks:
        left = 0
        right = len(sorted_tasks) - 1
        while left <= right:
            mid = (left + right) // 2
            if task.title.lower() < sorted_tasks[mid].title.lower():
                right = mid - 1
            else:
                left = mid + 1
        sorted_tasks.insert(left, task)
    # Step 2: Binary search in sorted_tasks to find the target title
    low = 0
    high = len(sorted_tasks) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_title = sorted_tasks[mid].title.lower()
        search_title = title.lower()

        if mid_title == search_title:
            return sorted_tasks[mid]
        elif mid_title < search_title:
            low = mid + 1
        else:
            high = mid - 1

    return None

# main
queue = TaskQueue()
while True: # validation of number of tasks
    try: 
        num_tasks = int(input('Kindly enter the number of tasks to create : '))
        if num_tasks > 0:
            break
        else:
            print('The number of tasks must be positive')
    except:
        print("Enter a valid int")

for i in range(num_tasks):
    print("\nTask " + str(i + 1) + ":")
    title = input("Enter task title: ")
    while True: # validation of duration
        try: 
            duration = int(input("Enter task duration (in mins): "))
            if duration > 0:
                break
            else:
                print('The duration must be positive')
        except:
            print("Enter a valid int")
    while True: # validation of priority
        try: 
            priority = int(input("Enter task priority (lower is higher): "))
            if priority > 0:
                break
            else:
                print('The priority must be a positive number')
        except:
            print("Enter a valid int")
    queue.insert(task(title, duration, priority))

print("\nAll Tasks in Queue:")
for task in queue.get_all_tasks():
    print(task)

print("\nSearch for a Task")
search_title = input("Enter the title to search for: ")
found = search_for_task(queue, search_title)
if found:
    print("Task found:", found)
else:
    print("Task not found.")

print("\nCompleting next highest priority task")
complete_next_task(queue)

print("\nSearch for a Task")
search_title = input("Enter the title to search for: ")
found = search_for_task(queue, search_title)
if found:
    print("Task found:", found)
else:
    print("Task not found.")

print("\nAll Tasks in Queue:")
for task in queue.get_all_tasks():
    print(task)
