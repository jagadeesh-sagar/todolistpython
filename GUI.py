import functions
import FreeSimpleGUI as sg
label1=sg.Text("Type in TO DO LIST")
input1=sg.InputText(tooltip="Enter TODO",key="Todo")
add_Button=sg.Button("Add")
window=sg.Window("MY TO-DO-LIST",layout=[[label1],[input1,add_Button]],font=('Arial',10))

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
        case sg.WIN_CLOSED:
            break


window.read()
window.close()