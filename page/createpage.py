import sys
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code')
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code\LOGIC')
import tkinter as tk
import task
import change
import APP
import main

#当前页面的任务
current_task=None

def on_click():
    pass

def delete():
    pass

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
        # 返回按钮
        button = tk.Button(return_mainpage, text="取消", command=on_click, bg='#A3C1C1', relief="flat")
        button.pack(side=tk.LEFT)

        # 删除按钮
        close_button = tk.Button(top_frame, text="X", command=delete, fg="red", bg='#A3C1C1', font=("Arial", 16, "bold"), width=4, height=2, relief="flat")
        close_button.pack(side=tk.RIGHT, padx=10, pady=10)

        #task_information
        task_information=tk.Frame(self,bg='#A3C1C1')
        task_information.pack()

        #title和勾选框
        task_top=tk.Frame(task_information,bg='#A3C1C1')
        task_top.grid(row=0,column=0)
        #is_finished=tk.
        title=tk.Entry(task_top)