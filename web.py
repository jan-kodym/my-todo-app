import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    if len(todo) > 0 and not (todo in todos):
        print("todo =", todo)
        print("todos =", todos)
        print("len(todo) =", len(todo))
        print("not (todo in todos) =", not (todo in todos))
        todos.append(todo)
        functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    # print(todo)
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:", label_visibility="hidden", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

print("Hello")

# st.session_state