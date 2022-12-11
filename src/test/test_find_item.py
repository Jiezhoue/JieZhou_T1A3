import pytest
from datetime import datetime

# this pytest is using to find the discount item based on day of the week
# And calculate the amount if user purchase 2 piece of item 1

date = {"Monday": "1",     
        "Tuesday": "2", 
        "Wednesday": "3", 
        "Thursday": "4", 
        "Friday": "5", 
        "Saturday": "6", 
        "Sunday": "7"
    }

items = {
    "1": {
        "name": "APPLE CRUMBLE CUPCAKE",
        "price": 5.5,
        "qty": 20
    },
    "2": {
        "name": "BANANA BREAD LATTE CUPCAKE",
        "price": 3.5,
        "qty": 2
    },
    "3": {
        "name": "CHOC VANILLA CUPCAKE",
        "price": 4.5,
        "qty": 40
    },
    "4": {
        "name": "RED VELVET CUPCAKE",
        "price": 8.5,
        "qty": 13
    },
    "5": {
        "name": "ROCKY ROAD CUPCAKE",
        "price": 7.5,
        "qty": 23
    }, 
    "6": {
        "name": "STRAWBERRY CUPCAKE",
        "price": 6,
        "qty": 10
    }, 
    "7": {
        "name": "MIX CHRISTMAS BOX",
        "price": 36,
        "qty": 8
    }
}

dt = datetime.now()

def find(list, day):
    for i in list:
        if i == day[dt.strftime('%A')]:
            return True

def amount(list, qty):
    return list["1"]["price"] * qty
    

def test_find():
    assert find(items, date) == True

def test_amount():
    assert amount(items, 2) == 11
