import sys
sys.path.append(r'C:\NJU总\NJU\大三上\软件工程\实验三\code\LOGIC')
import tasklist
import timelineview
from PIL import Image
import json
import os
import main

#打开时初始化
def Init():
    #用户头像
    main.image_path = r'data\uesr_photo.jpg'
    #用户姓名和格言
    with open('./data/user_information.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    main.user_name=data['user_name']
    main.user_tag=data['user_tag']
    main.user_task_list=tasklist.Task_list()
    main.user_task_list.load_from_file("data/user_data")
    #当前展示列表
    main.display_task_list=timelineview.TimelineView()
    main.display_task_list.display_daily(main.user_task_list)
    print(main.display_task_list.display_list)
    