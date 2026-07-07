
class Project:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def move_task():
        pass

class Column:
    
    def __init__(self, name):
        self.name = name
        self.task_list = []
    

    def add_task(self, task):
        self.task_list.append(task)


    def remove_task(self, task):
        self.task_list.remove(task)

    def __str__(self):
        return f"Column {self.name} has {self.task_list}."

class Task:

    def __init__(self, id: int, name: str, description: str, priority = 0):
        self.id = id
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"Task {self.id} - {self.name}: {self.description}. Priority: {self.priority}"