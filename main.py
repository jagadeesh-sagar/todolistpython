
while True:
    user_action=input('enter one option "add","show","completed"::')
    match user_action:
        case "add":
            todos=input("enter a todo list:")+"\n"
            todo=[]
            todo.append(todos)
            file1=open("todo.txt","a")
            file1.writelines(todo)

            file1.close()
        case "show":
            file1=open("todo.txt","r")
            c=file1.readlines()
            # c=[i.strip("\n") for i in c ]
            for index,i in enumerate(c,start=1):
              i=i.strip("\n")
              print(f"{index}.{i}")
            file1.close()
        case "exit"|"3" :
               print("exited from the todo list")
               break





