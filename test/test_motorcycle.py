import sys
sys.path.insert(0,'./function')
from motorcycle_db import MotorcycleDB

db = None

def setup_module(module):
    print("-----------------Connected-------------")
    global db
    db = MotorcycleDB()
    db.connect("data/data_file.json")

def teardown_module(module):
    print("-----------------Connected-------------")
    db.close()

def test_motorcycles_development_data():
    data = db.get_data("motorcycles")
    assert data["name"] == "motorcycles"
    assert data["id"] == 1
    assert data["price"] == 20000
    assert data["down_payment"] == 5000
    assert data["result"] == "pass"
    