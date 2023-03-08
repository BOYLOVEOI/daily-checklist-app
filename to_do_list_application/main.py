# Import Statements
import functions
import time

# Printing Date Stamp
time_stamp = time.strftime('%B %d, %Y %I:%M:%S %p')
print('It is', time_stamp)

while True:
    # Prompting the user for an action
    user_action = input("Type add, show, edit, complete, or exit: ")

    if user_action.strip().startswith('add'):
        
        # Calling the function get_todos to read the todos and create a todo_list 
        todo_list = functions.get_todos()
        
        # Retrieving ONLY the action task after the add keyword 
        todo = user_action.strip()[4:] + '\n'
        todo_list.append(todo) 
       
        # Overwriting the file object to be in 'write' mode to write the newly added contents in
        # the todo_list
        functions.write_todos(todo_list)

    elif user_action.strip().startswith('show'):
       
        todo_list = functions.get_todos() 
       
        for index, task in enumerate(todo_list):
            task = task.strip('\n')
            print(f"{index+1}. {task.title()}")

    elif user_action.strip().startswith('edit'):
       
        # Try-except block for error handling
        try:
           
            # Retrieving ONLY the edit number after the edit keyword 
            edit_item_number = int(user_action.strip()[5:])
            
            # Matching index with user input 
            index = edit_item_number - 1
            
            todo_list = functions.get_todos()

            
            # For the IndexError (to pop the message in case the user enters in an index outside range)
            todo_list[index]
            
            # New user-inputted task is then assigned to the desired edited task
            todo_list[index] = input("Please enter a new to-do: ") +'\n'
            
            # Updating the list with the newly edited item
            functions.write_todos(todo_list)

        
        # If user enters in 'edit [the command that they want to edit instead of the index/number]' 
        # we catch the ValueError and print out an error prompt
        except ValueError:
            print("Your command is not valid. Please enter in the NUMBER of the task that you want to edit.")
            continue
       
        # In case user enters in a edit task number that is not within the range of tasks in the list
        except IndexError:
            print("Please enter in a number of the task that is WITHIN the list.")
            continue

    elif user_action.strip().startswith('exit'):
        break 
    
    elif user_action.strip().startswith('complete'):
       
        # Try except block for error handling
        try:
           
            # Retrieving ONLY the complete number after the complete keyword 
            complete_number = int(user_action.strip()[9:])
            
            # Matching index with user input 
            index = complete_number - 1
            
            todo_list = functions.get_todos()
           
            # Retrieving completed todo to create a message indicating user has completed that task
            completed_task = todo_list[index].strip('\n')      
            
            # Popping the element from the list based on the index provided by the user 
            todo_list.pop(index)                                                                                                                          
            
            functions.write_todos(todo_list)

            print(f"Todo, {completed_task}, has been removed from the todo list.")
       
        except ValueError:
            print("Your command is not valid. Please enter in the NUMBER of the task that you want to complete.")
            continue
       
        # In case user enters in a number for the task that is NOT within the list's range
        except IndexError:
            print("Please enter in a number of the task that is WITHIN the list.")
            continue

    # In case user_action does not match any of the case statements above... 
    else:
        print("Input does not match any of the suggested choices... Please re-enter an action.")

print("Exiting...")
    








