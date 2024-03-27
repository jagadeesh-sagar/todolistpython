import os
while True:
    user_action=input('enter one option "add","show","exit","completed or use 1,2,3,4::')
    match user_action:
        case "add"|"1":
            todos=input("enter a todo list:")+"\n"
            todo=[]
            todo.append(todos)
            file1=open("todo.txt","a")
            file1.writelines(todo)
            file1.close()
        case "show"|"2":
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
        case "completed"|"4":
            file1=open("todo.txt","r")
            lines=file1.readlines()
            file1.close()
            completed1=input("enter the completed task:")

            for line in lines:
                if line.strip()!=completed1:
                     file2=open("todo2.txt","w")
                     file2.write(line)

            os.replace("todo2.txt","todo.txt")
            file2.close()
        case default:
            print("enter options between 1 to 3")





