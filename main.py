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
