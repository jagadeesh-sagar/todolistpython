import streamlit as st
import functions

todos=functions.read_todos()
def add_todo():
   todo=st.session_state['new_todo']+'\n'
   todos.append(todo)
   functions.write_todos(todos)


st.title("MY TO-DO APP")
st.subheader("This my TO-DO App")
st.write("This App help you to increase your productivity")
for todo in todos:
    st.checkbox(todo)
st.text_input(label="",placeholder="Add a New Todo",on_change=add_todo,key='new_todo')
st.session_state