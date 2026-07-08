""""""
class Project:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        #Create columns
        self.columns = {
            "to_do": Column("To do"),
            "in_progress": Column("In Progress"),
            "paused": Column("Paused"),
            "completed": Column("Completed")
        }

    def move_task(self, task, from_col_key, to_col_key):
        self.columns[from_col_key].remove_task(task)
        self.columns[to_col_key].add_task(task)

    def print_board(self):
        """Prindib konsooli kogu projekti visuaalse seisu koos tulpade ja ülesannetega."""
        print("\n" + "=" * 45)
        print(f" PROJEKT: {self.name.upper()}")
        print(f" Kirjeldus: {self.description}")
        print("=" * 45 + "\n")
        
        # Käime läbi kõik sõnastikus olevad tulbad
        for col_key, column in self.columns.items():
            # Prindime tulba nime ja sulgudesse ülesannete arvu
            print(f"--- {column.name} ({len(column.task_list)}) ---")
            
            # Kui tulbas pole ühtegi ülesannet
            if not column.task_list:
                print("  (Tulp on tühi)")
            else:
                # Kui on ülesanded, käime need läbi ja prindime reana
                for task in column.task_list:
                    # Kuna sul on Task klassis __str__ juba tehtud, 
                    # siis siin prinditaksegi see sinu kirjutatud ilus tekst.
                    print(f"  [ ] {task}")
            
            print() # Lisab tulpade vahele ühe tühja rea, et visuaalselt asja eraldada


    def __str__(self):
        return f"Project {self.name}: {self.description}."
    

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

    # id counter for testing purposes, increased every time constructor is called
    _id_counter = 1

    def __init__(self, name: str, description: str, priority = 0):
        self.id = self._id_counter
        self._id_counter += 1

        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"Task {self.id} - {self.name}: {self.description}. Priority: {self.priority}"
    
    def __repr__(self):
        return self.__str__()