import sys
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code')
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code\LOGIC')
import tkinter as tk
from task import *
from tkinter import *
from PIL import Image, ImageTk, ImageDraw
import task
import APP
import main
import viewpage

def refresh_today_task_list(today_task_list: tk.Frame):
    # Clear existing tasks
    for widget in today_task_list.winfo_children():
        widget.destroy()
    # Repopulate the task list
    show_today_task_list(today_task_list)

#显示当天任务
def show_today_task_list(today_task_list: tk.Frame):
    for item in main.display_task_list.display_list:
        task_frame=Frame(today_task_list,bg='black',width=300)
        task_frame.pack(pady=(10,10),fill="x")
        check_var = IntVar(value=1 if item.status == task.Status.COMPLETED else 0)  # 创建一个变量来存储复选框的状态
        finish_button=Checkbutton(task_frame,bg='black',variable=check_var,offvalue=0,onvalue=1,command=lambda: finish_task(item, check_var),highlightthickness=0,width=1)
        finish_button.grid(row=0,column=0,sticky=W)
        #title
        task_title=Label(task_frame,bg="black",text=item.title,fg='white',width=20)
        task_title.grid(row=0,column=1,sticky=W)
        #ddl
        formatted_date = item.ddl.strftime("%H:%M")
        task_ddl=Label(task_frame,bg='black',text=formatted_date,fg='white')
        task_ddl.grid(row=0,column=2)   

         
#创建新任务
def create_new_task(mainpage):
    #切换到createpage
    mainpage.controller.show_frame("Createpage")
    
    
#完成任务
def finish_task(current_task:task.Task,var:tk.BooleanVar):
    if var.get():
        current_task.status=task.Status.COMPLETED
    else:
        current_task.status=task.Status.TODO

#切换到任务组
def switch_task_group():
    pass
#切换到一览模式
def switch_view(mainpage):
    mainpage.controller.show_frame("Viewpage")

class Mainpage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg='#EAECDF')
        self.controller = controller
        #标题部分
        lab=Label(self,text="TODO Your Best",bg='#EAECDF',font=("Dokdo", 30,"bold"),fg="white")
        lab.pack(pady=(20,0))

        #用户栏部分
        user_total_frame=Frame(self,height=92,width=340,bg='#EAECDF')
        user_total_frame.pack(anchor=W,padx=(10,0),pady=(10,10))
        # 头像部分
        user_information=Canvas(user_total_frame,height=60,width=50,relief="raised",bg='#EAECDF',highlightthickness=0)
        user_photo=Image.open(main.image_path)
        user_photo=user_photo.resize((40,50))
        main.photo = ImageTk.PhotoImage(user_photo)
        user_picture=user_information.create_image(10,40,anchor=W,image=main.photo)
        user_information.grid(row=0,column=0,sticky="w")


        #格言和用户名部分
        user_frame=Frame(user_total_frame,bg='#EAECDF')
        name=Label(user_frame,text=main.user_name,bg='#EAECDF',compound="left",font=("Dokdo", 10),fg='grey')
        tag=Label(user_frame,text=main.user_tag,bg='#EAECDF',compound="left",font=("Dokdo", 10),fg='grey')
        user_frame.grid(row=0,column=1,sticky=W)
        name.grid(row=0,column=0,sticky="w")
        tag.grid(row=1,column=0)

        #功能区
        today_task=Frame(self,bg='#EAECDF',width=400,height=550)
        today_task.pack_propagate(0) 
        today_task.pack(pady=(10,0))
        #当天日期
        today = datetime.now()
        formatted_date = today.strftime("%A \n%Y年%m月%d日")
        current_day=Label(today_task,text=formatted_date,bg='#EAECDF')
        current_day.pack()
        #当天任务列表
        today_task_list=Frame(today_task,bg='#EAECDF')
        today_task_list.pack(fill=BOTH, expand=True)
        show_today_task_list(today_task_list)

        #刷新任务
        self.schedule_refresh(today_task_list)

        #创建新项目
        create_task=Button(today_task,text="创建新项目",command=lambda: create_new_task(self))
        create_task.pack(side=BOTTOM)

        #任务组
        task_group=Frame(self,bg='#EAECDF')
        task_group.pack(pady=(50,50),anchor=W)
        canvas = Canvas(task_group, width=50, height=20, bg='#EAECDF', highlightthickness=0)
        canvas.pack(side=LEFT, padx=(20, 0))
        canvas.create_line(5, 5, 25, 5, width=3)
        canvas.create_line(5, 11, 25, 11, width=3)
        canvas.create_line(5, 17, 25, 17, width=3)
        task_group_view = Button(task_group, text="查看任务组", bg='#EAECDF',command=switch_task_group)
        task_group_view.pack(side=LEFT, padx=(5, 0))

        #一览
        view=Frame(self,bg='#EAECDF')
        view.pack(pady=(0,10),anchor=W)
        canvas =Canvas(view, width=50, height=30, bg='#EAECDF', highlightthickness=0)
        canvas.pack(side=LEFT, padx=(20, 0))
        canvas.create_oval(5, 8, 25, 20, outline='black', width=2)  # 调整外圈
        canvas.create_oval(12, 11, 18, 17, fill='black')  # 内圈
        task_view = Button(view, text="任务一览", bg='#EAECDF',command=lambda:switch_view(self))
        task_view.pack(side=LEFT, padx=(5, 0))
    
    # Schedule the task list to refresh every 5 minutes
    def schedule_refresh(self, today_task_list):
        refresh_today_task_list(today_task_list)
        self.after(1000, lambda: self.schedule_refresh(today_task_list))  # 300000 ms = 5 minutes
        