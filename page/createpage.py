import sys
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code')
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code\LOGIC')
import tkinter as tk
import task
import change
import APP
import main


class Createpage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg='#A3C1C1')
        self.controller = controller
       
       # 创建一个画布，用于绘制箭头图标
        canvas = tk.Canvas(self, width=20, height=20, bg='lightblue', highlightthickness=0)
        canvas.create_line(15, 10, 5, 10, arrow=tk.LAST, fill='black')
        canvas.postscript(file='arrow.eps')
        canvas.grid(row=0, column=0)

        # 创建按钮，包含图标和文字
        button = tk.Button(root, text='取消', image=canvas_image, compound='left', command=on_click, bg='lightblue')
        button.image = canvas_image  # 保持对图像的引用
        button.grid(row=0, column=1)

