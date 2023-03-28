# Import Statements
import streamlit as st
import functions

# Function Creation 
def add_todo(to_do_list):
    # Retrieve the value stored in the input box through passing the key into the session_state dict
    task = st.session_state["-INPUT-"] + '\n'

    # Appending user inputted task to to_do_list
    to_do_list.append(task)
    
    # Writing the newly edited to_do_list to the task database
    functions.write_todos(to_do_list)

# Creation of the title label for the web app through the Title instance
st.title("My Todo App")

# Creation of subheader
st.subheader("Current tasks scheduled:")

# Retrieving task database as a list
to_do_list = functions.get_todos()

# Printing out the list of tasks as checkboxes (in case user wants to complete a task)
for x in to_do_list:
    # creating a st.checkbox variable that will hold each unique checkbox (with their corresponding task)
    # through assigning it a key y (the task itself)
    checkbox = st.checkbox(x, key = x)

    # if checkbox (which returns a bool) is True (or essentially the checkbox is checked)
    if checkbox:
        # Remove the checked checkbox (and, thereby, the task from to_do_list)
        to_do_list.remove(x)

        # Write the newly edited to_do_list to the task database
        functions.write_todos(to_do_list)

        # Delete the value from the session_state that has the key y (the task)
        del st.session_state[x]

        # Halts the script and requeues the script from the top
        st.experimental_rerun()

# Adding a text box for user input to add tasks 
# placeholder -> informs the user of the functionality of the input box
# on_change -> invokes a callback (which is an execution of code in response to an event) when the text_input's value changes (in our
# case, from "" to user input)
st.text_input(label="", placeholder="Enter a task", 
              key="-INPUT-", on_change=add_todo, args=(to_do_list,)) 

# In case I wanted to implement the 'Add' Button
# Adding the add button for users to add the tasks
# add_button = st.button('Add')

# The 'Add button logic
#if add_button == True:
    #task = st.session_state["-INPUT-"] + '\n'
    #to_do_list.append(task)
    #functions.write_todos(to_do_list)

# For bugging purposes... st.session_state is a dictionary that holds ALL the keys and their 
# corresponding values
# st.session_state


