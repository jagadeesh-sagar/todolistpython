import functions
import FreeSimpleGUI as sg
label1=sg.Text("Type in TO DO LIST")
input1=sg.InputText(tooltip="Enter TODO",key="Todo")
add_Button=sg.Button("Add")
list_box=sg.Listbox(values=functions.read_todos(),key="Todos",enable_events=True,size=[45,15])
Edit_Button=sg.Button("Edit")
complete_button=sg.Button("complete",key="completed")
Exit_button=sg.Button("Exit",key="exit")
window=sg.Window("MY TO-DO-LIST",layout=[[label1]
    ,[input1,add_Button],
    [list_box,Edit_Button,complete_button],
     [Exit_button]],font=('Arial',18))

while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.read_todos()
            new_todos=values['Todo'] +"\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['Todos'].update(values=todos)
        case "Edit":
            todo_to_edit=values['Todos'][0]

            new_todo=values['Todo']
            todo=functions.read_todos()
            index=todo.index(todo_to_edit)
            todo[index]=new_todo
            functions.write_todos(todo)
            window['Todos'].update(values=todo) #update is used for updating the listboxes in real time
        case "completed":
            todos_completed=values['Todos'][0]
            todos=functions.read_todos()
            todos.remove(todos_completed)
            functions.write_todos(todos)
            window['Todos'].update(values=todos)
            window['Todo'].update(value="")
        case "Todos":
            window['Todo'].update(values['Todos'][0])
        case "exit":
            window.close()
            break
        case sg.WIN_CLOSED:
            exit()


window.read()
window.close()