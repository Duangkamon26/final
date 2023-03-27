import json

class MotorcycleDB:
    def __init__(self):
        self.data = None

    def connect(self, data_files):
        with open(data_files) as json_files:
            self.data = json.load(json_files)

    def get_data(self, name):
        for motorcycle in self.data["motorcycles"]:
            if motorcycle["name"] == name:
                return motorcycle

    def close(self):
        pass