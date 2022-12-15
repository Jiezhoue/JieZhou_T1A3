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
        "qty": 1
    },
    "3": {
        "name": "CHOC VANILLA CUPCAKE",
        "price": 4.5,
        "qty": 2
    },
    "4": {
        "name": "RED VELVET CUPCAKE",
        "price": 8.5,
        "qty": 1
    },
    "5": {
        "name": "ROCKY ROAD CUPCAKE",
        "price": 7.5,
        "qty": 1
    }, 
    "6": {
        "name": "STRAWBERRY CUPCAKE",
        "price": 6,
        "qty": 1
    }, 
    "7": {
        "name": "MIX CHRISTMAS BOX",
        "price": 36,
        "qty": 1
    }
}


def find(list, week, day):
    for i in list:
        if i == week[day]:
            return i


def amount(date_file, history_dict, day):
    total_amount = 0
    for i in history_dict: # loop all the items in shopping cart when checkout and calculate the total amount
        if i == date_file[day]: # check each item if it's on discount or not based on today's special
            total_amount = total_amount + history_dict[i]['qty'] * (history_dict[i]['price']*(1-0.2))
        else:
            total_amount = total_amount + history_dict[i]['qty'] * history_dict[i]['price']
                
    return total_amount

def test_find():
    assert find(items, date, "Saturday") == "6"

def test_amount():
    assert amount(date, items, "Sunday") == 65.3
