# Import Statements
import functions
import PySimpleGUI as sg 

# Label for the window (HAS TO BE A STRING)
label = sg.Text("Type in a task")

# InputText() is an input text box... tooltip = tip that appears as user's mouse hovers text box
input_box = sg.InputText(tooltip = "Enter task")

# Creating an event button, to add tasks
add_button = sg.Button('Add')

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
window = sg.Window("Daily Checklist", layout=[[[label],[input_box,add_button]]])
window.read()

# It is imperative that you close the window through the close() method
window.close()