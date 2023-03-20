# Import Statements
import functions 
import PySimpleGUI as sg 
import time

# Adding a theme for the window
sg.theme(new_theme='Black')

# Label for the window (HAS TO BE A STRING)
label = sg.Text("Type in a task")

# Label for the timestamp
label_time = sg.Text("", key='-TIME-')

# InputText() is an input text box... tooltip = tip that appears as user's mouse hovers text box
input_box = sg.InputText(tooltip = "Enter task", key='-TASK-')

# Creating a box to output already stored tasks
list_box = sg.Listbox(values=functions.get_todos(), size=(45,10), key='-ITEMS-', 
                      enable_events=True)

# Creating an event button, to add tasks
add_button = sg.Button('Add', size=8)

# Creating an event button, to edit tasks
edit_button = sg.Button('Edit', size=8)

# Creating an event button, to complete tasks
complete_button = sg.Button('Complete', size=8)

# Creating an event button, to exit tasks
exit_button = sg.Button('Exit', size=8)

# As we now have a label for the window and inpux text box for the window we must now pass them into
# the Window() object so we can connect them together

# Window() may look like a function call, but is actually an object/instance of PySimpleGUI
# First argument for the Window Object is a title for the window
# Why must the syntax of the layout=argument be [[]]? -> layout= takes a nested list (list within a list)
# of button or text objects. The layout=argument is assembled in a row format meaning that one row 
# within the window is an inner list within the layout=argument syntax. Thus, [[label],[input_box]] creates
# 2 rows within the window for there are two inner lists. As it is sequentially-ordered, the label row
# is on top of the input_box row. BUT in [[label, input_box]] there is only one row for there is only one
# inner list.
window = sg.Window("Daily Checklist", 
                    layout=[[label_time],
                            [label],
                            [input_box,add_button], 
                            [list_box, edit_button, complete_button], 
                            [exit_button]],
                    font=('Helvetica', 10))

while True:
    # window.read() returns a tuple of the button label and the input box 
    # (returned as a dict of key, -TASK-, and user-inputted value)
    # timeout=200 -> window is being read every 200 miliseconds                                                                                                                
    event, values = window.read(timeout=200)                                                                          

    # Updating the timestamp
    window['-TIME-'].update(value=time.strftime('%B %d, %Y %I:%M:%S %p'))
    
    match event:
        # If user presses add
        case 'Add':         
            to_do_list = functions.get_todos()
            
            # In case user wants to add MULTIPLE of the same tasks in their schedule
            if values['-TASK-'] in to_do_list:
                new_to_do = values['-TASK-']
            
            # Else if user is not adding a duplicate task...
            else:
                new_to_do = values['-TASK-'] + '\n'
            
            to_do_list.append(new_to_do)
            functions.write_todos(to_do_list)

            # Updating an added item to the list box
            window['-ITEMS-'].update(values=to_do_list)
            
        # If user exits the window manually                                                                                                                                                                                  
        case sg.WINDOW_CLOSED:
            break

        # If user presses edit
        case 'Edit': 
            # try and except block to catch an index error
            try:
                old_task = values['-ITEMS-'][0]
                new_task = values['-TASK-'] + '\n'

                to_do_list = functions.get_todos()
                old_task_index = to_do_list.index(old_task)
                to_do_list[old_task_index] = new_task

                functions.write_todos(to_do_list)

                # Refreshing the list box to show the edited item
                window['-ITEMS-'].update(values=to_do_list)

            except IndexError:
                error_message = 'Please select a task to edit!'
                
                # Pop up window to relay error message
                sg.popup(error_message, font=('Helvetica', 10))

            except ValueError:
                error_message = 'Please enter a different and unique task as your edited task!'
                sg.popup(error_message, font=('Helvetica', 10))
        
        # If user presses complete
        case 'Complete':
            # try and except block to catch an index error
            try: 
                completed_task = values['-ITEMS-'][0]
                
                to_do_list = functions.get_todos()
                to_do_list.remove(completed_task)

                functions.write_todos(to_do_list)                   

                # Updating the window after a user completes a task
                window['-ITEMS-'].update(values=to_do_list)

                # Refreshing the input box after user completes an item
                window['-TASK-'].update(value='')

            except IndexError:
                error_message = "Please select a task to complete!"
                sg.popup(error_message, font=('Helvetica', 10))
        
        # If user presses exit
        case 'Exit':
            break
            
        # Having the selected item appear in the input box (for easier edit)
        case '-ITEMS-':
            # In case user selects an empty -ITEMS- value
            try:
                window['-TASK-'].update(value=values['-ITEMS-'][0].strip('\n'))
            
            except IndexError:
                error_message = 'Please populate the task list!'
                sg.popup(error_message, font=('Helvetica', 10))
  
# It is imperative that you close the window through the close() method
window.close()      