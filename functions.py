FILEPATH = "todos.txt"




def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

#def write_todos(filepath, todos_arg):
def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
    return


if __name__ == "__main__":
    print("Hello from functions")