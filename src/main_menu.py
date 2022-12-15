from os import system
import os.path
import json
from functions import *
from history import item
from datetime import datetime
import time

try:
    from art import *
except ImportError:
    raise ImportError("The art package is not installed")



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
        input("Press return to contine.....")



date = {"Monday": "1",                      # discount item no. based on today's date
        "Tuesday": "2", 
        "Wednesday": "3", 
        "Thursday": "4", 
        "Friday": "5", 
        "Saturday": "6", 
        "Sunday": "7"
    }


with open("original.txt") as f:
        data = f.read()
origial_dict = json.loads(data)             # read the stock items from txt file and assign to variable original_dict as a dictionary

if os.path.exists("cart.txt"):              # check if the shopping cart is empty or not from the last exit
    with open("cart.txt") as f:
        cart_data = f.read()
        cart_dict = json.loads(cart_data)
else:
    cart_dict = {}

# if cart_dict != {}:                         # adjust the quantity of stock items based on the existing shopping cart items
#     for key in cart_dict:
#         origial_dict[key]["qty"] = origial_dict[key]["qty"] - cart_dict[key]["qty"]

option = ""

time.sleep(4)                               # wait for 5 second before execute the program

while option != "5": 
    
    system("clear") 
    welcome()                               # shop ASCII title using art package
    try:
        option = int(main_menu())           # return user input
    except ValueError:                      # if the user input is alphabet, prompt ValueError message
        system("clear") 
        print("Please enter a valid integer 1-5")
        input("Press return to continue......")
        continue
        
    if option == 1:
        system("clear")
        select= ""
        while select!="m":
            system("clear")
            print("================================================================================")
            tprint("Cupecake Menu")     # ASCII subtitle
            print("================================================================================")

            select = item_menu(origial_dict, date)
            
            if select in origial_dict:  # check if the user input exist in stock items dictionory key value
                system("clear")
                tprint("Cupecake Menu")
                buy_item(select)        # add item into shopping cart and decrease the quantity of that item in stock              
                input("Press return to contine.....")
                continue
            elif select == "m":
                break
            else:
                system("clear")
                tprint("Cupecake Menu")
                print("This item no does not exist, please input correct item no...")
                input("Press return to contine.....")
    
    elif option == 2:
        system("clear")
        choice = ""
        while choice != "m":
            system("clear")
            print("=======================================================================")
            tprint("Items In Cart")
            print("=======================================================================")
            choice = cart_menu(cart_dict)   # display the shopping cart items
            if choice == False:             # shopping cart is empty
                input("You don't have any items in the shopping cart, press return back to main menu....")
                break
            elif choice in cart_dict:
                delete_item(choice)
            elif choice != "m":
                system("clear")
                tprint("Items In Cart")
                print("Item no is wrong, please imput the correct item no..")
                input("Press return to contine.....")
                continue

    elif option == 3:
        system("clear")
        print("==========================================")
        tprint("Receipt")
        print("==========================================")
        if len(cart_dict) != 0:             # checkout and display the receipt
            display_receipt(date, cart_dict)
            cart_dict = {}                  # after checkout, empty the shopping cart
            input("Press return to continue........")
        else:
            print("There is no item in cart.....")
            input("Press return to continue........")
            continue  
    
    elif option == 4:
        system("clear")
        print("============================================================================================")
        tprint("Purchase History")
        print("============================================================================================")
        if os.path.exists("receipt.txt"):   # check if user has purchased any items or not
            receipt_file = open("receipt.txt", "r")
            line_list = receipt_file.readlines()
            for line in line_list:
                print(line)
            input("Press return to continue.......")
        else:
            print("There is no history record.....")
            input("Press return to continue.......")
            continue
    
    elif option == 5: # exit the program
        system("clear")
        print("=======================================================================================================================================")
        tprint("Thanks for your purchase")
        tprint("See you next time!")
        print("=======================================================================================================================================")
        break
    else:
        system("clear")
        print("The input menu no. is invalid, please input the valid menu no. (1-5)")
        input("Press return to continue..........")


if len(cart_dict) != 0:                         # before exit, check the shopping cart and save the items in txt file
    with open("cart.txt", "w") as outfile:
        json.dump(cart_dict, outfile)
elif os.path.exists("cart.txt"):                # if the shopping cart is empty, remove the file
    os.remove("cart.txt")

with open("original.txt", "w") as outfile:
    json.dump(origial_dict, outfile)