# Global Variables
FILE_PATH = r'C:\Users\paull\OneDrive\Desktop\Python Projects\to_do_list_application\todos.txt'

# Function Declaration 
def get_todos(text_file=FILE_PATH):
    """Reads in a text file and returns a list of to-do items"""
    with open(text_file, 'r') as file:
        todo_local_list = file.readlines()
    return todo_local_list

def write_todos(todo_list_local, text_file=FILE_PATH):
    """Opens a text file and writes onto it the contents of a passed in list"""
    with open(text_file, 'w') as file:
        file.writelines(todo_list_local)
print(__name__)
# If you want to test specific lines of code and NOT have in executed in your main module (where your
# importing the module from) you need to have the following if conditional block
if __name__ == '__main__':
    print('hello')