FILEPATH= "todo.txt"
def read_todos(filepath=FILEPATH):
    with open(filepath, "r") as files:
        todos = files.readlines()
    return todos


def write_todos(todos,filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos)
if __name__=="__main__":
    print("hello")
