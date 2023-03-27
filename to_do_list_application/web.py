# Import Statements
import streamlit as st
import functions

# Creation of the title label for the web app through the Title instance
st.title("My Todo App")

# Creation of subheader
st.subheader("Current tasks scheduled:")

to_do_list = functions.get_todos()
checkbox_list = []

# Printing out the list of tasks as checkboxes (in case user wants to complete a task)
for x in to_do_list:
    checkbox_list.append(st.checkbox(x))

# Adding a text box for user input to add tasks 
# placeholder -> informs the user of the functionality of the input box
add_box = st.text_input(label="", placeholder="Enter a task", key='-INPUT-') 

# Adding the add button for users to add the tasks
add_button = st.button('Add')




