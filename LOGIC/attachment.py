class Attachment:
    def __init__(self, file_name: str, file_data: bytes):
        self.file_name = file_name
        self.file_data = file_data

    def delete(self):
        # Delete logic
        pass