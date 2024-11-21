from ctypes.wintypes import HTASK
from datetime import datetime,timedelta,date
from enum import Enum
from typing import List

# Enums for Status and Priority
class Status(Enum):
    TODO = 'TODO'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'

class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

# User Module
class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.devices = []

    def register(self):
        # Registration logic
        pass

    def login(self):
        # Login logic
        pass

    def sync(self):
        # Sync logic
        pass

class Device:
    def __init__(self, device_id: str):
        self.device_id = device_id



# Task Module
class Task:
    def __init__(self, 
                 num: int,
                 title: str="", 
                 description: str="", 
                 task_class: str="",
                 ddl: datetime=datetime.now(), 
                 priority: Priority=Priority.LOW,
                 status: Status=Status.TODO):
        self.task_num=num
        self.title = title
        self.description = description
        self.task_class = task_class
        self.ddl = ddl
        self.priority = priority
        self.status = status
        self.reminders = []
        self.attachments = []

    def create(self):
        # Create task logic
        pass

    def edit(self, **kwargs):
        # Update task attributes based on kwargs
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def delete(self):
        # Delete task logic
        pass
    


#存储所有任务
class task_list():
    def _init_(self):
        self.tasklist=[]

    def add_task(self,**kwargs):
        next_num=self.tasklist.count()+1
        task=Task(num=next_num)
        self.tasklist.append(task)
        task.edit(kwargs)

    def delete_task(self,title:str):
        for it in self.tasklist:
            if it.title==title:
                self.tasklist.remove(it)

   

class TaskGroup:
    def __init__(self, name: str):
        self.name = name
        self.is_active = True
        self.tasks = []

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def sort_by_priority(self):
        #按照优先级排序
        self.tasks.sort(key=lambda task: task.priority.value)

    def sort_by_ddl(self):
        #按照ddl排序
        self.tasks.sort(key=lambda task: task.ddl)

class RecurringTask(Task):
    def __init__(self, 
                 title: str="", 
                 description: str="", 
                 task_class: str="",
                 ddl: datetime=datetime.now(), 
                 priority: Priority=Priority.LOW,
                 status: Status=Status.TODO,
                 recurringfrequency: timedelta=timedelta(days=7)
                 ):
        super().__init__(self,title,description,task_class,ddl,priority,status)
        self.recurringfrequency=recurringfrequency

    def remove_recurrence(self):
        # Remove recurrence logic
        pass

    def update_reminder(self):
        # Update reminder logic
        pass

class Attachment:
    def __init__(self, file_name: str, file_data: bytes):
        self.file_name = file_name
        self.file_data = file_data

    def delete(self):
        # Delete logic
        pass

class Reminder:
    def __init__(self, num:int, reminder_time: datetime, is_active: bool):
        self.num=num
        self.reminder_time = reminder_time
        self.is_active = is_active

    def set_reminder(self, reminder_time: datetime):
        self.reminder_time = reminder_time
        self.is_active = True

    def delete_reminder(self):
        self.is_active = False

    def remind(self):
        # Reminder logic
        pass

# View Module
class TimelineView:
    def __init__(self):
        self.display_list=[]

    def display_daily(self):
        self.display_list.clear()
        for item in task_list.tasklist:
            if item.DDL==date.today():
                self.display_list.append(item)

    def display_weekly(self):
        self.display_list.clear()
        today = date.today()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        for item in task_list.tasklist:
            if start_of_week <= item.DDL <= end_of_week:
                self.display_list.append(item)

    def display_monthly(self):
        # Display monthly tasks
        pass

    def display_all(self):
        # Display all tasks
        pass
