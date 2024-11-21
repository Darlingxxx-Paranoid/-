import tkinter as tk
from tkinter import ttk

def sync():
    print("同步任务")

root = tk.Tk()
root.title("TODO Your Best")
root.geometry("375x812")
root.configure(bg="#F5F5DC")

# 顶部栏
top_frame = tk.Frame(root, bg="#F5F5DC")
top_frame.pack(fill=tk.X, pady=10)

user_label = tk.Label(top_frame, text="QYY", font=("Arial", 14), bg="#F5F5DC")
user_label.pack(side=tk.LEFT, padx=10)

sync_button = tk.Button(top_frame, text="同步", command=sync, bg="#F5F5DC")
sync_button.pack(side=tk.RIGHT, padx=10)

quote_label = tk.Label(root, text="已完成的课题不会在生命中重现", font=("Arial", 10), bg="#F5F5DC")
quote_label.pack(pady=5)

# 日期
date_label = tk.Label(root, text="星期六\n2024年10月26日", font=("Arial", 12), bg="#F5F5DC")
date_label.pack(pady=5)

# 任务列表
tasks = [
    ("软件工程作业", "完成需求采集的设计", "今天10:00"),
    ("打乒乓球", "记得带球拍", ""),
    ("睡前冥想电脑更新", "同步重要思维", "")
]

for task_title, task_desc, task_time in tasks:
    task_frame = tk.Frame(root, bg="#F5F5DC", pady=5)
    task_frame.pack(fill=tk.X, padx=10)

    task_label = tk.Label(task_frame, text=task_title, font=("Arial", 12), bg="#F5F5DC")
    task_label.pack(side=tk.LEFT)

    time_label = tk.Label(task_frame, text=task_time, font=("Arial", 10), bg="#F5F5DC")
    time_label.pack(side=tk.RIGHT)

    desc_label = tk.Label(task_frame, text=task_desc, font=("Arial", 10), bg="#F5F5DC")
    desc_label.pack()

# 底部按钮
bottom_frame = tk.Frame(root, bg="#F5F5DC")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)

create_button = tk.Button(bottom_frame, text="创建新项目", bg="#333", fg="#FFF")
create_button.pack(fill=tk.X, padx=20, pady=5)

view_group_button = tk.Button(bottom_frame, text="查看任务组", bg="#333", fg="#FFF")
view_group_button.pack(fill=tk.X, padx=20, pady=5)

task_list_button = tk.Button(bottom_frame, text="任务一览", bg="#333", fg="#FFF")
task_list_button.pack(fill=tk.X, padx=20, pady=5)

root.mainloop()

