from datetime import datetime
class Reminder:
    def __init__(self, num:int, reminder_time: datetime, is_active: bool):
        self.num=num
        self.reminder_time = reminder_time
        self.is_active = is_active

    def set_reminder(self, reminder_time: datetime):
        self.reminder_time = reminder_time
        self.is_active = True

    def close_reminder(self):
        self.is_active = False

    def remind(self):
        # Reminder logic
        pass
    #转化为字典
    def to_dict(self):
        return {
            "num": self.num,
            "reminder_time": self.reminder_time.isoformat(),
            "is_active": self.is_active
        }
    #从字典恢复
    @staticmethod
    def from_dict(data):
        return Reminder(
            num=data["num"],
            reminder_time=datetime.fromisoformat(data["reminder_time"]),
            is_active=data["is_active"]
        )