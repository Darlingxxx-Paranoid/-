import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Page App")

        # 创建容器 Frame
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # 存储不同页面的字典
        self.frames = {}

        # 初始化页面
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # 将所有页面放在同一位置
            frame.grid(row=0, column=0, sticky="nsew")

        # 显示初始页面
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        # 切换页面
        frame = self.frames[page_name]
        frame.tkraise()



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Page One")
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Go to Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Page Two")
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Go to Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


