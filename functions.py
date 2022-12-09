from art import *
import pandas
from history import item
from datetime import datetime

def main_menu():
    print("1. Show Menu")
    print("2. Go to Cart")
    print("3. Checkout")
    print("4. Show the history")
    print("5. exit the program")
    opt = input("Please select the option(1-5): ")
    return opt

def welcome():
    print("=========================================================================================================")
    tprint("The Classic Cupcake")
    print("=========================================================================================================")

def items_display(js):
    df = pandas.DataFrame.from_dict(js, orient='index')
    print(df)

def item_menu(list):
    items_display(list)
    select=input('Please input Cupcake item number (1,2,3...) to purchase the item or enter "m" back to main menu: ')
    return select  

def cart_menu(list):
    if len(list) != 0:
        items_display(list)
        select = input("Input item number to delete the item from your cart or enter m to back to main menu: ")
        return select
    else:
        return False

def display_receipt(date, cart_items):
    new = item.add_history(item, date, cart_items)
    return new