from ctypes.wintypes import HTASK
from datetime import datetime,timedelta,date
from enum import Enum
from typing import List
import json
import reminder
import attachment

# Enums for Status and Priority
class Status(Enum):
    TODO = 'TODO'
    IN_PROGRESS = 'IN_PROGRESS'
    COMPLETED = 'COMPLETED'

class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

# Task Module
class Task:
    def __init__(self, 
                 title: str="新任务", 
                 description: str="", 
                 task_class: str="",
                 ddl: datetime=datetime.now(), 
                 priority: Priority=Priority.LOW,
                 status: Status=Status.TODO):
        self.title = title
        self.description = description
        self.task_class = task_class
        self.ddl = ddl
        self.priority = priority
        self.status = status
        self.attachments_list = []
        self.reminder_list =[]
        default_reminder=reminder.Reminder(1,self.ddl,is_active=1)
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
        new_reminder=reminder.Reminder(total_num+1,remind_time,is_active=1)
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
    #以字典形式输出
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "task_class": self.task_class,
            "ddl": self.ddl.isoformat(),  # Convert datetime to string
            "priority": self.priority.value,
            "status": self.status.value,
            "reminder_list": [reminder.to_dict() for reminder in self.reminder_list]
        }

    @staticmethod
    def from_dict(data):
        task= Task(
            title=data["title"],
            description=data["description"],
            task_class=data["task_class"],
            ddl=datetime.fromisoformat(data["ddl"]),
            priority=Priority(data["priority"]),
            status=Status(data["status"])
        )
        task.reminder_list = [reminder.Reminder.from_dict(reminder_data) for reminder_data in data["reminder_list"]]
        return task

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
    
    #以字典形式输出
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "task_class": self.task_class,
            "ddl": self.ddl.isoformat(),  # Convert datetime to string
            "priority": self.priority.value,
            "status": self.status.value,
            "recurringfrequency": self.recurringfrequency,
            "reminder_list": [reminder.to_dict() for reminder in self.reminder_list]
        }

    @staticmethod
    def from_dict(data):
        task= RecurringTask(
            title=data["title"],
            description=data["description"],
            task_class=data["task_class"],
            ddl=datetime.fromisoformat(data["ddl"]),
            priority=Priority(data["priority"]),
            status=Status(data["status"]),
            recurringfrequency=data["recurringfrequency"]
        )
        task.reminder_list = [reminder.Reminder.from_dict(reminder_data) for reminder_data in data["reminder_list"]]
        return task





