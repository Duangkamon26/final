
import sys
sys.path.insert(0,'./function')
from customer_db import CustomerDB

db = None

def setup_module(module):
    print("-----------------Connected-------------")
    global db
    db = CustomerDB()
    db.connect("data/data_file.json")

def teardown_module(module):
    print("-----------------Connected-------------")
    db.close()

def test_win_data():
    data = db.get_data("Win")
    assert data["name"] == "Win"
    assert data["id"] == 1


    