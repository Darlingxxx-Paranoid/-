import sys
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code\page')
import sys
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code\page')
import init
import APP
import tasklist
import timelineview
#头像
photo=None
#用户头像路径
image_path=None
#用户名字和格言
user_name=None
user_tag=None
#用户任务列表
user_task_list: tasklist.Task_list = None
#当前界面展示任务列表
display_task_list:timelineview.TimelineView=None


if __name__ == "__main__":
    init.Init()
    root = APP.App()
    root.mainloop()