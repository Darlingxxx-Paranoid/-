import tkinter as tk
import mainpage
import createpage

user_picture=None

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TODO Your Best")
        
        # 创建容器 Frame
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # 存储不同页面的字典
        self.frames = {}

        # 初始化页面
        for F in (mainpage.Mainpage,createpage.Createpage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # 将所有页面放在同一位置
            frame.grid(row=0, column=0, sticky="nsew")

        # 显示初始页面
        self.show_frame("Mainpage")

    def show_frame(self, page_name):
        # 切换页面
        frame = self.frames[page_name]
        frame.update()
        frame.tkraise()