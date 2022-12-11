from art import *
import pandas
from history import item
from datetime import datetime

def main_menu(): # return the user input from the main menu
    print("1. Show Menu")
    print("2. Go to Cart")
    print("3. Checkout")
    print("4. Show purchase history")
    print("5. Exit the program")
    opt = input("Please select the option(1-5): ")
    return opt

def welcome(): # ASCII text title from art package
    print("=========================================================================================================")
    tprint("The Classic Cupcake") 
    print("=========================================================================================================")

def items_display(js): # pandas package to display items in table
    df = pandas.DataFrame.from_dict(js, orient='index')
    print(df)

def item_menu(list, date_file): # display the stock items
    items_display(list)
    dt = datetime.now()
    print("------------------------------------------------------------------")
    for i in list:
        if i == date_file[dt.strftime('%A')]:
            print(f'{dt.strftime("%A")} Special, {list[i]["name"]} 20% off')
    print("------------------------------------------------------------------")
    select=input('Please input Cupcake item number (1,2,3...) to purchase the item or enter "m" back to main menu: ')
    return select  

def cart_menu(list): # display the shopping cart items
    if len(list) != 0:
        items_display(list)
        select = input("Input item number to delete the item from your cart or enter m to back to main menu: ")
        return select
    else:
        return False # if no item in shopping cart, return false

def display_receipt(date, cart_items): 
    new = item.add_history(item, date, cart_items) # use function inside self created Class to display the receipt and added into txt file for record
    return new