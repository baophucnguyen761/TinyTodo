import itertools
from datetime import date
from dataclasses import dataclass
from typing import Optional
from enum import IntEnum

class Priority(IntEnum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

@dataclass
class TaskItem:
    id: int
    description: str
    created: date
    due: Optional[date] = None
    completed: bool = False
    priority: Priority = Priority.MEDIUM

    _item_id_iter = itertools.count(1)

    # by default tasks have no due date and medium (2) priority
    @classmethod
    def create_item(cls, description: str,
               due: Optional[date] = None,
               priority: Priority = Priority.MEDIUM) -> 'TaskItem':
        return cls(
            id=next(cls._item_id_iter), # get id from iter & increment
            description=description,
            created=date.today(),
            due=due,
            completed=False,
            priority=priority
        )
    
    # update counter per max id after loading tasks from save file
    @classmethod
    def reset_id_counter(cls, items: list['TaskItem']):
        last_id = max((item.id for item in items), default=0)
        cls._item_id_iter = itertools.count(last_id + 1)

class TodoList:
    _list_id_counter = itertools.count(1) # track list ids

    def __init__(self, id: int, name: str, tasks: Optional[list[TaskItem]] = None):
        self.id = id
        self.name = name
        self.tasks: list[TaskItem] = tasks if tasks is not None else []
        # index for quick task lookup
        self._index: dict[int, TaskItem] = {task.id: task for task in self.tasks}

    def add_task(self, task: TaskItem):
        self.tasks.append(task)
        self._index[task.id] = task 

    def get_task(self, task_id: int) -> Optional[TaskItem]:
        return self._index.get(task_id)

    def remove_task(self, task_id: int):
        task = self._index.pop(task_id, None)
        if task:
            self.tasks.remove(task)

    def complete_task(self, task_id: int):
        task = self.get_task(task_id)
        if task:
            task.completed = True
    
    def set_priority(self, task_id: int, priority: Priority):
        task = self.get_task(task_id)
        if task:
            task.priority = priority

    def set_due(self, task_id: int, due: date):
        task = self.get_task(task_id)
        if task:
            task.due = due
    
    @classmethod
    def create_list(cls, name: str, tasks: Optional[list[TaskItem]] = None) -> 'TodoList':
        return cls(next(cls._list_id_counter), name, tasks)
    
    @classmethod
    def load_list(cls, data:dict) -> 'TodoList':
        tasks = [
            TaskItem(
                id=task_data['id'],
                description=task_data['description'],
                created=date.fromisoformat(task_data['created']),
                due=date.fromisoformat(task_data['due']) if task_data['due'] else None,
                completed=task_data['completed'],
                priority=Priority(task_data['priority'])
            ) for task_data in data['tasks']
        ]
        return cls(data['id'], data['name'], tasks)

    @classmethod
    def reset_id_counter(cls, lists: list['TodoList']):
        last_id = max((lst.id for lst in lists), default=0)
        cls._list_id_counter = itertools.count(last_id + 1)
