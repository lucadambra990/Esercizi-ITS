from datetime import datetime, date
class Data:
    def __init__(self, data:str):
        self.data = data.strptime(data, '%Y-%m-%d %H:%M:%S')

class Database:
    def __init__(self):
        self.data:Data
    def add_data(self, new_data:Data):
        self.data = new_data

