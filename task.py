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


class Reminder:
    def __init__(self, num:int, reminder_time: datetime, is_active: bool):
        self.num=num
        self.reminder_time = reminder_time
        self.is_active = is_active

    def set_reminder(self, reminder_time: datetime):
        self.reminder_time = reminder_time
        self.is_active = True

    def close_reminder(self):
        self.is_active = False

    def remind(self):
        # Reminder logic
        pass

# Task Module
class Task:
    def __init__(self, 
                 num: int,
                 title: str="新任务", 
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
        self.attachments_list = [Attachment]
        self.reminder_list =[Reminder]
        default_reminder=Reminder(1,self.ddl,is_active=1)
        self.reminder_list.append(default_reminder)

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
    #添加提醒
    def add_reminder(self,remind_time: datetime):
        total_num=len(self.reminders)
        new_reminder=Reminder(total_num+1,remind_time,is_active=1)
        self.reminder_list.append(new_reminder)

    #关闭提醒
    def delete_reminder(self,reminder_num: int):
        for item in self.reminder_list:
            if item.num==reminder_num:
                item.close_reminder()

    #删除提醒
    def delete_reminder(self,reminder_num: int):
        for item in self.reminder_list:
            if item.num==reminder_num:
                self.reminder_list.remove(item)
    #
    def add_attachment(self):
        pass
    


#存储所有任务
class task_list():
    def __init__(self):
        self.tasklist=[]

    def add_task(self,**kwargs):
        next_num=len(self.tasklist)+1
        task=Task(num=next_num)
        self.tasklist.append(task)
        task.edit(**kwargs)

    def delete_task(self,title:str):
        for it in self.tasklist:
            if it.title==title:
                self.tasklist.remove(it)
                break

   

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



# View Module
class TimelineView:
    def __init__(self):
        self.display_list=[]

    def display_daily(self,task_list:task_list):
        self.display_list.clear()
        for item in task_list.tasklist:
        # 将 ddl 转换为日期对象
            item_date = item.ddl.date()            
            if item_date == date.today():  # 比较任务的日期和今天的日期
                self.display_list.append(item)

    def display_weekly(self,task_list:task_list):
        self.display_list.clear()
        today = date.today()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        for item in task_list.tasklist:
            if start_of_week <= item.DDL <= end_of_week:
                self.display_list.append(item)
                break

    def display_monthly(self):
        # Display monthly tasks
        pass

    def display_all(self):
        # Display all tasks
        pass
