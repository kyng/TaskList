
class Project:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def move_task():
        pass

class Column:
    
    def __init__(self, name):
        self.name = name
        task_list = []
    

    def add_task():
        pass

    def remove_task():
        pass

    def __str__(self):
        pass

class Task:

    def __init__(self, id: int, name: str, description: str, priority = 0):
        self.id = id
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"Task {self.id} - {self.name}: {self.description}. Priority: {self.priority}"