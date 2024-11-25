import sys
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code')
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code\LOGIC')
import tkinter as tk
import task
import APP
import main
import reminder
import tasklist

#当前页面的任务
current_task=task.Task()
#完成任务
def finish_task(var:tk.BooleanVar):
    global current_task
    if var.get():
        current_task.status=task.Status.COMPLETED
    else:
        current_task.status=task.Status.TODO

def back(page):
    #切换到Mainpage
    page.controller.show_frame("Mainpage")
    

def delete(task,page):
    page.controller.show_frame("Mainpage")

def save(page):
    global current_task
    main.user_task_list.add_task(current_task)
    print(current_task.description)
    # main.user_task_list.save_to_file("data/user_data")
    page.controller.show_frame("Mainpage")

class Createpage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg='#A3C1C1')
        self.controller = controller

        

         # 主框架
        top_frame = tk.Frame(self, bg='#A3C1C1')
        top_frame.pack(fill=tk.X)

        # 返回
        return_mainpage = tk.Frame(top_frame, bg='#A3C1C1')
        return_mainpage.pack(side=tk.LEFT, padx=10, pady=10)
        canvas = tk.Canvas(return_mainpage, width=20, height=20, bg='#A3C1C1', highlightthickness=0)
        canvas.create_line(0, 10, 20, 10, arrow=tk.FIRST, fill='black', width=4)
        canvas.pack(side=tk.LEFT)
        #取消按钮
        button = tk.Button(return_mainpage, text="取消", command=lambda: back(self), bg='#A3C1C1', relief="flat")
        button.pack(side=tk.LEFT)

        #保存按钮
        close_button = tk.Button(top_frame, text="保存", command=lambda: save(self), bg='#A3C1C1', font=("Arial", 16, "bold"), width=4, height=2, relief="flat")
        close_button.pack(side=tk.RIGHT, padx=10, pady=10)

        #task_information
        task_information=tk.Frame(self,bg='#A3C1C1')
        task_information.pack()

        #title和勾选框
        task_top=tk.Frame(task_information,bg='#A3C1C1')
        task_top.grid(row=0,column=0)
        check_var = tk.IntVar(value=1 if current_task.status == task.Status.COMPLETED else 0)  # 创建一个变量来存储复选框的状态
        finish_button=tk.Checkbutton(task_top,bg='#A3C1C1',variable=check_var,offvalue=0,onvalue=1,command=lambda: finish_task(check_var),highlightthickness=0,width=10)
        finish_button.grid(row=0,column=0)
        title=tk.Entry(task_top,bg='#A3C1C1',relief="flat")
        title.insert(0,current_task.title)
        #获取当前标题
        current_task.title=title.get()
        title.grid(row=0,column=1)

        #信息区域
        information_field=tk.Frame(task_information,bg='#A3C1C1')
        information_field.grid(row=1,pady=(20,10))
        #任务描述
        task_1=tk.Label(information_field,bg='#A3C1C1',text="描述：")
        task_1.grid(row=0,column=0)
        task_description=tk.Entry(information_field,bg='#A3C1C1',relief='flat')
        task_description.insert(0,current_task.description)
        #获取当前描述
        current_task.description=task_description.get()
        task_description.grid(row=0,column=1,pady=(20,20))

        #任务紧急度
        task_2=tk.Label(information_field,bg='#A3C1C1',text="Priority: ")
        task_2.grid(row=1,column=0)
        #显示任务紧急度
        var=tk.StringVar()
        if current_task.priority == task.Priority.LOW:
            var.set("low")
        elif current_task.priority == task.Priority.MEDIUM:
            var.set("medium")
        elif current_task.priority == task.Priority.HIGH:
            var.set("high")
        task_priority=tk.OptionMenu(information_field,var,"low","medium","high")
        #获取当前标题
        if var.get()=="low":
            current_task.priority=task.Priority.LOW
        elif var.get()=="medium":
            current_task.priority=task.Priority.MEDIUM
        elif var.get()=="high":
            current_task.priority=task.Priority.HIGH
        task_priority.grid(row=1,column=1,pady=(20,20))

        #任务提醒
        task_3=tk.Label(information_field,bg='#A3C1C1',text="提醒: ")
        task_3.grid(row=2,column=0)
        #提醒修改和添加
        def add():
            #TODO
            pass
        def edit():
            #TODO
            pass
        formatted_date = current_task.reminder_list[0].reminder_time.strftime("%Y年%m月%d日 %H:%M")
        reminder_display=tk.Label(information_field,bg='#A3C1C1',text=formatted_date)
        reminder_display.grid(row=2,column=1,pady=(20,20))

        #recurring模式
        #TODO

        #附件区域
        task_4=tk.Label(information_field,bg='#A3C1C1',text="附件: ")
        task_4.grid(row=3,column=0)
        if len(current_task.attachments_list) == 0:
            #添加附件
            attachment_button=tk.Button(information_field,bg='#A3C1C1',text="点击以添加附件",relief="flat")
            attachment_button.grid(row=3,column=1,pady=(20,20))
        else:
            #展示附件
            #TODO
            pass
        
        #分类区域
        task_5=tk.Label(information_field,bg='#A3C1C1',text="任务分类: ")
        task_5.grid(row=4,column=0)
        if current_task.task_class == "":
            #添加附件
            taskclass=tk.Button(information_field,bg='#A3C1C1',text="点击以添加分类",relief="flat")
            taskclass.grid(row=4,column=1,pady=(20,20))
        else:
            taskclass=tk.Label(information_field,bg='#A3C1C1',text=current_task.task_class)
            taskclass.grid(row=4,column=1,pady=(20,20))
            pass

        #删除按钮
        delete_button=tk.Button(information_field,bg="red",text="删除",relief="flat",width=20,command=lambda: delete(self))
        delete_button.grid(row=5, column=0, columnspan=2, pady=(20, 20))
