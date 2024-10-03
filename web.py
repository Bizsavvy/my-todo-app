import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    if todo_local:
        todos.append(todo_local.capitalize())
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""


st.title("My To-Do App")
st.subheader("This is my to-do app")
st.write("This app will increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a new to-do...",
              on_change= add_todo, key="new_todo")