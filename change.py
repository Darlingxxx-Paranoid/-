import task
#创建新任务
def create_new_task():
    pass
#完成任务
def finish_task(current_task:task.Task):
    current_task.status=task.Status.COMPLETED   
#切换到任务组
def switch_task_group():
    pass
#切换到一览模式
def switch_view():
    pass