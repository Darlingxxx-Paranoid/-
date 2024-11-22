import task
import json
#存储所有任务
class Task_list():
    def __init__(self):
        self.tasklist=[]
        self.classlist={}

    def add_task(self,task:task.Task):
        self.tasklist.append(task)
        self.classlist.update(task.task_class)

    def delete_task(self,title:str):
        for it in self.tasklist:
            if it.title==title:
                self.tasklist.remove(it)
                break
    #删除某个类
    def delete_class(self,task_class:str):
        self.classlist-{task_class}
    #储存task
    def save_to_file(self, filepath: str):
        with open(filepath, 'w', encoding='utf-8') as f:
            data = {
                "tasks": [task.to_dict() for task in self.tasklist],
                "classlist": self.classlist
            }
            json.dump(data, f, ensure_ascii=False, indent=4)

    #恢复task
    def load_from_file(self, filepath: str):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tasklist = [task.Task.from_dict(task_data) for task_data in data.get("tasks", [])]
                self.classlist = data.get("classlist", {})
        except FileNotFoundError:
            print(f"File {filepath} not found. Starting with an empty task list.")
    