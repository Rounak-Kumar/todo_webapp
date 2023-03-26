import streamlit as st
import functions
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

st.title("My todo app")

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo']
    todos.append(new_todo + '\n')
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''


def complete_todo(todo_arg):
    todos.remove(todo_arg)
    functions.write_todos(todos)
    del st.session_state[todo_arg]


for todo in todos:
    checkbox = st.checkbox(label=todo, key=todo)
    if checkbox:
        complete_todo(todo)
        st._rerun()

st.text_input(label='', placeholder="Add a todo...", key='new_todo', on_change=add_todo)
