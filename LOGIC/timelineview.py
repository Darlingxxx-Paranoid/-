import tasklist
from datetime import datetime,date,timedelta
# View Module
class TimelineView:
    def __init__(self):
        self.display_list=[]

    def display_daily(self,task_list:tasklist.Task_list):
        self.display_list.clear()
        for item in task_list.tasklist:
        # 将 ddl 转换为日期对象
            item_date = item.ddl.date()            
            if item_date == date.today():  # 比较任务的日期和今天的日期
                self.display_list.append(item)

    def display_weekly(self,task_list:tasklist.Task_list):
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
