import sys
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code')
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code\LOGIC')
import tkinter as tk
import timelineview
import tasklist

def back(page):
    #切换到Mainpage
    page.controller.show_frame("Mainpage")


def refresh_displaytasklist(display_frame: tk.Frame):
    # Clear existing tasks
    for widget in display_frame.winfo_children():
        widget.destroy()
    # Repopulate the task list
    display(display_frame)

def display(display_frame:tk.Frame):
    global displaylist
    for item in displaylist.display_list:
        task_frame=tk.Frame(display_frame,bg="black")
        task_frame.pack(pady=(10,10),fill="x")
        task_title=tk.Label(task_frame,bg="black",text=item.title,fg='white',width=20)
        task_title.grid(row=0,column=0)
        #ddl
        formatted_date = item.ddl.strftime("%H:%M")
        task_ddl=tk.Label(task_frame,bg='black',text=formatted_date,fg='white')
        task_ddl.grid(row=0,column=1) 
    
#切换展示列表
def switch(option,option_frame:tk.Frame,display_frame):
    global opt
    #按钮展示切换
    if option==opt:
        pass
    else:
        for widget in option_frame.winfo_children():
            if widget.widgetName=="button":
                if widget["text"] ==opt:
                    widget.configure(bg="#EDE1D9",fg="black")
                elif widget["text"]==option:
                    widget.configure(bg='black',fg="white")
        opt=option
    #任务列表切换
    global displaylist
    global current_tasklist
    current_tasklist.tasklist.clear()
    current_tasklist.load_from_file("data/user_data")
    if opt=="今天":     
        displaylist.display_daily(current_tasklist)
    elif opt=="本周":
        displaylist.display_weekly(current_tasklist) 
    display(display_frame)

#当前预览模式选项    
opt=None
#当前任务列表
current_tasklist=tasklist.Task_list()
current_tasklist.load_from_file("data/user_data")
#当前展示列表
displaylist=timelineview.TimelineView()
displaylist.display_daily(current_tasklist)

class Viewpage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg='#EDE1D9')
        self.controller = controller

        #顶部区域框架
        top_frame = tk.Frame(self, bg='#EDE1D9')
        top_frame.pack(fill=tk.X)

        # 返回
        return_mainpage = tk.Frame(top_frame, bg='#EDE1D9')
        return_mainpage.pack(side=tk.LEFT, padx=(10,10),pady=(10,10))
        canvas = tk.Canvas(return_mainpage, width=20, height=20, bg='#EDE1D9', highlightthickness=0)
        canvas.create_line(0, 10, 20, 10, arrow=tk.FIRST, fill='black', width=4)
        canvas.pack(side=tk.LEFT)
        #取消按钮
        button = tk.Button(return_mainpage, text="返回主页面", command=lambda: back(self), bg='#EDE1D9', relief="flat")
        button.pack(side=tk.LEFT)


        # 创建选项框容器
        option_frame = tk.Frame(self, bg='#EAE1D9')
        option_frame.pack(pady=10)

        # 添加“预览模式”标签
        preview_label = tk.Label(option_frame, text="预览模式", bg='#EAE1D9', fg='black')
        preview_label.grid(row=0,column=0)

        # 定义其他选项
        options = ["今天", "本周", "本月", "全部"]
        
        #当前选项
        global opt
        opt="今天"
        #当前列号
        column_num=1
        # 创建选项按钮
        for option in options:
            if opt==option:
                btn = tk.Button(
                    option_frame, 
                    text=option, 
                    bg='black', 
                    fg='white', 
                    relief='flat',
                    command=lambda current_option=option:switch(current_option,option_frame,display_field)
                )
                btn.grid(padx=10,row=0,column=column_num)
                column_num+=1
            else:   
                btn = tk.Button(
                    option_frame, 
                    text=option, 
                    bg='#EAE1D9', 
                    fg='black', 
                    relief='flat',
                    command=lambda current_option=option:switch(current_option,option_frame,display_field)
                )
                btn.grid(padx=10,row=0,column=column_num)
                column_num+=1

        # 下划线
        black = tk.Frame(option_frame, bg='black', height=2,width=100)
        black.grid(row=1,column=0)  
        black = tk.Frame(option_frame, bg='grey', height=2,width=260)
        black.grid(row=1,column=1,columnspan=4,sticky="W") 

        display_field=tk.Frame(self,bg='#EAE1D9')
        display_field.pack(pady=(10,10),fill='both')
        self.schedule_refresh(display_field)

    def schedule_refresh(self, display_field):
        refresh_displaytasklist(display_field)
        self.after(1000, lambda: self.schedule_refresh(display_field))    