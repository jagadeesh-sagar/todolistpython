def read_todos():
    with open("todo.txt", "r") as files:
        todos = files.readlines()
    return todos


def write_todos(todos):
    with open("todo.txt", "w") as file:
        file.writelines(todos)
