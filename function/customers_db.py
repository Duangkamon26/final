import json

class CustomerDB:
    def __init__(self):
        self.data = None

    def connect(self, data_files):
        with open(data_files) as json_files:
            self.data = json.load(json_files)

    def get_data(self, name):
        for customer in self.data["customer"]:
            if customer["name"] == name:
                return customer

    def close(self):
        pass