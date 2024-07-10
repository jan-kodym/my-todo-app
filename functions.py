FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Nacte to-do ze souboru a vrati jejich list """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_to_write, filepath=FILEPATH):
    """ Ulozi list to-do do souboru """
    with open(filepath, 'w') as file:
        file.writelines(todos_to_write)


def vypsat_todos_cli():
    """ Nacte to-do ze souboru a vypise ocislovany seznam do standardniho vystupu """
    todos = get_todos()
    for i, todo in enumerate(todos):
        print(f"{i + 1} - {todo.strip()}")


if __name__ == "__main__":
    print(__name__)
    print(get_todos())