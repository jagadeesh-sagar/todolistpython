def read_todos():
    with open("todo.txt", "r") as file:
        todos = file.readlines()
    return todos
def write_todos(todos):
    with open("todo.txt", "w") as file:
        file.writelines(todos)
while True:
    user_action = input('Enter one option\n1.add\n2.show\n3.completed\n4.exit\nCan also use  options names:')
    match user_action:
        case "add" | "1":
            todo = input("Enter a todo: ") + "\n"
            todos = read_todos()
            todos.append(todo)
            write_todos(todos)
        case "show" | "2":
            todos = read_todos()
            for index, todo in enumerate(todos, start=1):
                print(f"{index}. {todo.strip()}")
        case "completed" | "3":
            todos = read_todos()
            completed_task = input("Enter the completed task: ")
            updated_todos = [todo for todo in todos if todo.strip() != completed_task]
            write_todos(updated_todos)
        case "exit" | "4":
            print("Exited from the todo list")
            break
        case _:
            print("Enter options between 1 to 4")
