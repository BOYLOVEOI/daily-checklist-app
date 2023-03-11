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
# Why must the syntax of the layout argument be [[]]? -> layout takes a list of button or textbox objects
# HOWEVER, the layout is assembled in a row format... [[label, input_box]] means one row of a label and
# input_box... BUT if you wanted to rows you would do [[layout],[input_box]]... each inner list represents
# a row in the window 
window = sg.Window("Daily Checklist", layout=[[[label],[input_box,add_button]]])
window.read()

# It is imperative that you close the window through the close() method
window.close()