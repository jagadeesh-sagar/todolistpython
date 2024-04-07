def read_todos():
    with open("todo.txt", "r") as file:
        todos = file.readlines()
    return todos
def write_todos(todos):
    with open("todo.txt", "w") as file:
        file.writelines(todos)
while True:
   user_action = input('Type add,show,completed,edit,exit::')
   user_action.strip()

   if "add" in user_action:
        todo = user_action[4:]+"\n"
        todos = read_todos()
        todos.append(todo)
        write_todos(todos)
   elif "show" in user_action:
        todos = read_todos()
        for index, todo in enumerate(todos, start=1):
            print(f"{index}. {todo.strip()}")
   elif "completed" in user_action:
        todos = read_todos()
        completed_task = user_action[10:]
        updated_todos = [todo for todo in todos if todo.strip() != completed_task] # list comprehension
        """  updated_todos = []
                for todo in todos:
                    if todo.strip() != completed_task:
                        updated_todos.append(todo)"""
        """ num=input("enter a index of todo ")
            todos.pop(num-1)
            write_todos(todos)""" # another way of doing
        write_todos(updated_todos)

   elif "edit" in user_action:
          print("")
          todos=read_todos()
          for index, todo in enumerate(todos, start=1):
            print(f"{index}. {todo.strip()}")
          num=int(input("enter a index  :"))-1
          updated_todos = [todo for todo in todos]
          updated_todos[num]=input("enter the todo: ")+'\n'
          write_todos(updated_todos)
          for index, todo in enumerate(updated_todos, start=1):
            print(f"{index}. {todo.strip()}")
   elif "exit" in user_action :
        print("Exited from the todo list")
        break
   else:
        print("Enter options between 1 to 4")

