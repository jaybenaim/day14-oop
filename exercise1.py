class Task: 
    def __init__(self, description, due_date): 
        self.description = description 
        self.due_date = due_date 

    def __repr__(self): 
        return f'{self.description} {self.due_date}'

# print(project1) 

class TodoList(Task): 
    def __init__(self, description, due_date): 
        super().__init__(description, due_date)
    def add_task(self): 
        new_task = Task(self.description, self.due_date) 

todoList = [] 

project1 = Task('create a first project', "August 12, 2019")
project2 = Task('create a second project', "August 14, 2019")
project3 = Task('create a third project', "August 10, 2019")
test2 = TodoList('call eden', 'tomorrow')
todoList.append(project1) 
todoList.append(project2) 
todoList.append(project3) 
todoList.append(test2)


for task in todoList: 
    print(f'* {task}') 

# print(test2)

