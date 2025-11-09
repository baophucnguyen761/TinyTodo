import json
from datetime import date
from schemas import TaskItem, TodoList, Priority

def save_lists(lists: list[TodoList], filename="todo_lists.json"):
    data = []
    for lst in lists:
        list_data = {
            'id': lst.id,
            'name': lst.name,
            'tasks': [
                {
                    'id': task.id,
                    'description': task.description,
                    'created': task.created.isoformat(),
                    'due': task.due.isoformat() if task.due else None,
                    'completed': task.completed,
                    'priority': task.priority.value
                } for task in lst.tasks
            ]
        }
        data.append(list_data)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_lists(filename='todo_lists.json') -> list[TodoList]:
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        lists = [TodoList.load_list(list_data) for list_data in data]
        items = [task for lst in lists for task in lst.tasks]
        TaskItem.reset_id_counter(items)
        TodoList.reset_id_counter(lists)
        return lists
    except FileNotFoundError:
        return []