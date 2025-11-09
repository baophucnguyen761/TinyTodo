from datetime import date
from schemas import TodoList, TaskItem, Priority
from todo import save_lists, load_lists

if __name__ == "__main__":
    # Load existing todo lists
    todo_lists = load_lists()

    # Example usage: create a new todo list and add tasks
    new_list = TodoList.create_list("My New Todo List")
    task1 = TaskItem.create_item("Buy groceries", due=date(2024, 7, 1), priority=Priority.HIGH)
    task2 = TaskItem.create_item("Read a book", priority=Priority.LOW)

    new_list.add_task(task1)
    new_list.add_task(task2)

    todo_lists.append(new_list)

    # Save the updated todo lists
    save_lists(todo_lists)