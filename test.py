import sys
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code\LOGIC')
import tasklist
import task

task1=task.Task(title="123")
task2=task.Task(title="345")
user_task_list=tasklist.Task_list()
user_task_list.add_task(task1)
user_task_list.add_task(task2)
user_task_list.load_from_file("user1")
user_task_list.save_to_file("user2")