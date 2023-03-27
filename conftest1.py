import sys
sys.path.insert(0,'./function')
from customer_db import CustomerDB 
from pytest import fixture

@fixture(scope="module")
def db():
    print("-----------------Connected-------------")
    db = CustomerDB()
    db.connect("data/data_file.json")
    yield db 
    print("---------close----------")
    db.close()