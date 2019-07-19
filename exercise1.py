class Task: 
    def __init__(self, description, due_date): 
        self.description = description 
        self.due_date = due_date 

    def __repr__(self): 
        return f'{self.description} {self.due_date}'

# print(project1) 

class TodoList: 
    
    def __init__(self): 
        self.todoList = [] 
        
    def __str__(self): 
        return f'{self.todoList}'

    def __repr__(self): 
        return f'{self.todoList}'

    def add_task(self, task): 
        self.todoList.append(task) 


task1 = Task('dad','asda')
task2 = Task('dad','asda')
task3 = Task('dad','asda')
list1 = TodoList()
list1.add_task(task1) 
list1.add_task(task2) 
list1.add_task(task3) 
print(list1) 



        # new_task = Task(self.description, self.due_date)
        # todoList.append(new_task) 
        # print(todoList) 
        





# project1 = Task('create a first project', "August 12, 2019")
# project2 = Task('create a second project', "August 14, 2019")
# project3 = Task('create a third project', "August 10, 2019")
# test2 = TodoList('call eden', 'tomorrow')
# todoList.append(project1) 
# todoList.append(project2) 
# todoList.append(project3) 
# todoList.append(test2)



# print(test2)

