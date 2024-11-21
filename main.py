from task import *
from tkinter import *
from PIL import Image, ImageTk, ImageDraw

#创建新项目
def create_new_task():
    user_task.add_task()

#显示当天任务
def show_today_task_list():
    display_task_list.display_daily(user_task)   
    for item in display_task_list.display_list:
        task_frame=Frame(toady_task_list,bg='black',width=300)
        task_frame.pack(pady=(10,10),anchor=W)
        check_var = IntVar()  # 创建一个变量来存储复选框的状态
        check_var.set(0)  # 初始化变量为未选中状态
        check_button=Checkbutton(task_frame,bg='black',text=f"{item.title}",fg='white',variable=check_var,onvalue=1,offvalue=0,command=finish_task(item),highlightthickness=0,width=10)
        formatted_date = item.ddl.strftime("%H:%M")
        task_ddl=Label(task_frame,bg='black',text=formatted_date,fg='white',width=20)
        task_ddl.grid(row=0,column=1)
        check_button.grid(row=0,column=0,sticky=W)
#完成任务
def finish_task(task:Task):
    task.status=Status.COMPLETED
#切换到任务组
def switch_task_group():
    pass
#切换到一览模式
def switch_view():
    pass
    
#用户的所有任务列表
user_task=task_list()
user_task.add_task(title="软工作业")
user_task.add_task(title="大创")
#当前展示的任务列表
display_task_list=TimelineView()

#初始化窗口
root=Tk()
root.title('To-Do-Best')
root.geometry('440x956')
root.config(bg="#EAECDF")

#标题部分
lab=Label(root,text="TODO Your Best",bg='#EAECDF',font=("Dokdo", 30,"bold"),fg="white")
lab.pack(pady=(20,0))

#用户栏部分
user_total_frame=Frame(root,height=92,width=340,bg='#EAECDF')
user_total_frame.pack(anchor=W,padx=(10,0),pady=(10,10))
# 头像部分
user_information=Canvas(user_total_frame,height=60,width=50,relief="raised",bg='#EAECDF',highlightthickness=0)
image_path = "C:/Users/-Darlingxxx/Desktop/报名照片.jpg"    #头像路径
image=Image.open(image_path)
image=image.resize((40,50))
photo = ImageTk.PhotoImage(image)
user_picture=user_information.create_image(10,40,anchor=W,image=photo)
user_information.grid(row=0,column=0,sticky="w")

#格言和用户名部分
user_frame=Frame(user_total_frame,bg='#EAECDF')
name="YQY"
tag="已完结的课题不会在生命中重现"
user_name=Label(user_frame,text=name,bg='#EAECDF',compound="left",font=("Dokdo", 10),fg='grey')
user_tag=Label(user_frame,text=tag,bg='#EAECDF',compound="left",font=("Dokdo", 10),fg='grey')
user_frame.grid(row=0,column=1,sticky=W)
user_name.grid(row=0,column=0,sticky="w")
user_tag.grid(row=1,column=0)

#功能区
today_task=Frame(root,bg='#EAECDF',width=400,height=550)
today_task.pack_propagate(0) 
today_task.pack(pady=(10,0))
#当天日期
today = datetime.now()
formatted_date = today.strftime("%A \n%Y年%m月%d日")
current_day=Label(today_task,text=formatted_date,bg='#EAECDF')
current_day.pack()
#当天任务列表
toady_task_list=Frame(today_task,bg='#EAECDF')
toady_task_list.pack(fill=BOTH, expand=True)
show_today_task_list()

#创建新项目
create_task=Button(today_task,text="创建新项目",command=create_new_task)
create_task.pack(side=BOTTOM)

#任务组
task_group=Frame(root,bg='#EAECDF')
task_group.pack(pady=(50,50),anchor=W)
canvas = Canvas(task_group, width=50, height=20, bg='#EAECDF', highlightthickness=0)
canvas.pack(side=LEFT, padx=(20, 0))
canvas.create_line(5, 5, 25, 5, width=3)
canvas.create_line(5, 11, 25, 11, width=3)
canvas.create_line(5, 17, 25, 17, width=3)
task_group_view = Button(task_group, text="查看任务组", bg='#EAECDF',command=switch_task_group)
task_group_view.pack(side=LEFT, padx=(5, 0))

#一览
view=Frame(root,bg='#EAECDF')
view.pack(pady=(0,10),anchor=W)
canvas =Canvas(view, width=50, height=30, bg='#EAECDF', highlightthickness=0)
canvas.pack(side=LEFT, padx=(20, 0))
canvas.create_oval(5, 8, 25, 20, outline='black', width=2)  # 调整外圈
canvas.create_oval(12, 11, 18, 17, fill='black')  # 内圈
task_view = Button(view, text="任务一览", bg='#EAECDF',command=switch_view)
task_view.pack(side=LEFT, padx=(5, 0))

root.mainloop()
