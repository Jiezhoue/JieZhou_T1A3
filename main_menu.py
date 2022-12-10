from os import system
from art import *
import os.path
import json
from functions import *
from history import item
from datetime import datetime


def buy_item(item_no):
    if origial_dict[item_no]["qty"] == 0:
        print("Item not in stock......Please select other items")
    else:
        if item_no in cart_dict:
            cart_dict[item_no]["qty"] += 1
            origial_dict[item_no]["qty"] -= 1
            print(f'1 {cart_dict[item_no]["name"]} has been added to your cart.')
        else:
            cart_dict[item_no] = origial_dict[item_no].copy()
            cart_dict[item_no]["qty"] = 1
            origial_dict[item_no]["qty"] -= 1
            print(f'1 {cart_dict[item_no]["name"]} has been added to your cart.')

def delete_item(item_no):
    if cart_dict[item_no]["qty"] > 0:
        cart_dict[item_no]["qty"] -= 1
        if cart_dict[item_no]["qty"] == 0:
            cart_dict.pop(item_no)
        origial_dict[item_no]["qty"] += 1
    else:
        print("The item no is wrong, please select again....")
        input("enter to contine.....")




date = {"Monday": "1",     # discount based on today's date
        "Tuesday": "2", 
        "Wednesday": "3", 
        "Thursday": "4", 
        "Friday": "5", 
        "Saturday": "6", 
        "Sunday": "7"
    }

with open("original.txt") as f:
        data = f.read()
origial_dict = json.loads(data) # read the stock items from txt file and assign to variable original_dict as a dictionary

if os.path.exists("cart.txt"): # check if the shopping cart is empty or not from the last exit
    with open("cart.txt") as f:
        cart_data = f.read()
        cart_dict = json.loads(cart_data)
else:
    cart_dict = {}

if cart_dict != {}: # adjust the quantity of stock items based on the existing shopping cart items
    for key in cart_dict:
        origial_dict[key]["qty"] = origial_dict[key]["qty"] - cart_dict[key]["qty"]

option = ""


while option != "5": 
    system("clear") 
    welcome() # shop ASCII title using art package
    
    option = main_menu() # return user input
    if option == "1":
        system("clear")
        select= ""
        while select!="m":
            system("clear")
            tprint("Cupecake Menu") # ASCII subtitle
            select = item_menu(origial_dict, date)
            
            if select in origial_dict: # check if the user input exist in stock items dictionory key value
                system("clear")
                tprint("Cupecake Menu")
                buy_item(select) # add item into shopping cart and decrease the quantity of that item in stock              
                input("Press Enter to contine.....")
                continue
            elif select == "m":
                break
            else:
                system("clear")
                tprint("Cupecake Menu")
                print("incalid input....")
                input("enter to contine.....")
    
    elif option =="2":
        system("clear")
        choice = ""
        while choice != "m":
            system("clear")
            tprint("Items In Cart")
            choice = cart_menu(cart_dict) # display the shopping cart items
            if choice == False: # shopping cart is empty
                input("You don't have any items in the shopping cart, press enter to return to main menu....")
                break
            elif choice in cart_dict:
                delete_item(choice)
            elif choice != "m":
                system("clear")
                tprint("Items In Cart")
                print("Item no is wrong, please imput the correct item no..")
                input("enter to contine.....")
                continue

    elif option =="3":
        system("clear")
        tprint("Receipt")
        if len(cart_dict) != 0: # checkout and display the receipt
            display_receipt(date, cart_dict)
            cart_dict = {} # after checkout, empty the shopping cart
            input("enter to continue........")
        else:
            print("There is no item in cart.....")
            input("enter to continue........")
            continue  
     
    elif option =="4":
        system("clear")
        tprint("Purchase History")
        if os.path.exists("receipt.txt"): # check if user has purchased any items or not
            receipt_file = open("receipt.txt", "r")
            line_list = receipt_file.readlines()
            for line in line_list:
                print(line)
            input("enter to continue........")
        else:
            print("There is no history record.....")
            input("enter to continue........")
            continue
    
    elif option =="5": # exit the program
        system("clear")
        tprint("Thanks for your purchase.")
        break

    else:
        print("The input is invalid, please input the valid menu no.")
        system("clear")

tprint("See you next time!")

if len(cart_dict) != 0: # before exit, check the shopping cart and save the items in txt file
    with open("cart.txt", "w") as outfile:
        json.dump(cart_dict, outfile)
elif os.path.exists("cart.txt"): # if the shopping cart is empty, remove the file
    os.remove("cart.txt")