import sys
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code\LOGIC')
import task
import tasklist
import main
import APP
import mainpage
import tkinter as tk

#创建新任务
def create_new_task(mainpage):
    new_task=task.Task()
    #添加新任务
    main.user_task_list.add_task(new_task)
    #切换到createpage
    mainpage.controller.show_frame("Createpage")
    
    
#完成任务
def finish_task(current_task:task.Task,var:tk.BooleanVar):
    if var.get():
        current_task.status=task.Status.COMPLETED
        print("ok")   
    else:
        current_task.status=task.Status.TODO
        print("no") 

#切换到任务组
def switch_task_group():
    pass
#切换到一览模式
def switch_view():
    pass