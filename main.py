import functions
while True:
    user_action = input('Type add,show,completed,edit,exit::')
    user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]+"\n"
        todos = functions.read_todos()
        todos.append(todo)
        functions.write_todos(todos)
    elif user_action.startswith("show"):
        todos = functions.read_todos()
        for index, todo in enumerate(todos, start=1):
            print(f"{index}. {todo.strip()}")
    elif user_action.startswith("completed"):
        completed_task = user_action[10:].strip()
        todos = functions.read_todos()
        if any(todo.strip() == completed_task for todo in todos): #if any (): returns True or False
            updated_todos = [todo for todo in todos if todo.strip() != completed_task]
            functions.write_todos(updated_todos)

        """  updated_todos = []
                for todo in todos:
                    if todo.strip() != completed_task:
                        updated_todos.append(todo)"""
        """ num=input("enter a index of todo ")
            todos.pop(num-1)
            write_todos(todos)""" # another way of doing

    elif user_action.startswith("edit"):
           try:
                  print("")
                  todos=functions.read_todos()
                  for index, todo in enumerate(todos, start=1):
                    print(f"{index}. {todo.strip()}")
                  num=int(user_action[5:])-1
                  updated_todos = [todo for todo in todos]
                  updated_todos[num]=input("enter the todo: ")+'\n'
                  functions.write_todos(updated_todos)
                  for index, todo in enumerate(updated_todos, start=1):
                    print(f"{index}. {todo.strip()}")
           except ValueError:
               print("Your command is not valid")

           except IndexError:
               print("index is not valid ")

    elif user_action.startswith("exit"):
        print("Exited from the todo list")
        break
    else:
        print("Enter valid options:")


