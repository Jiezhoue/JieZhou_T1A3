from os import system
from art import *
import os.path
import json
from functions import *
from history import item
from datetime import datetime



def buy_item(item_no):
    if origial_dict[item_no]["qty"] == 0:
        print("No item in stock......Please select other items")
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


def display_receipt():
    new = item.add_history(item, date, cart_dict)
    return new


date = {"Monday": "1", "Tuesday": "2", "Wednesday": "3", "Thursday": "4", "Friday": "5", "Saturday": "6", "Sunday": "7"}


with open("original.txt") as f:
        data = f.read()

file = json.loads(data)

option = ""

origial_dict = {}

origial_dict = file
cart_dict = {}

while option != "5":
    system("clear")
    welcome()

    option = main_menu()

    if option == "1":
        system("clear")
        select= ""
        while select!="m":
            system("clear")

            tprint("Cupecake Menu")

            select = item_menu(origial_dict)
            if select in origial_dict:
                system("clear")
                tprint("Cupecake Menu")
                buy_item(select)
            
                
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

            choice = cart_menu(cart_dict)
            if choice == False:
                input("You don't have any items in the shopping cart, press enter to return to main menu....")
                break
            elif choice in cart_dict:
                print("aaaa")
                delete_item(choice)
            elif choice != "m":
                system("clear")
                tprint("Items In Cart")
                print("Item no is wrong, please imput the correct item no..")
                input("enter to contine.....")
                continue


    elif option =="3":
        system("clear")
        tprint("Reciept")

        if len(cart_dict) != 0:
            display_receipt()
            cart_dict = {}
            input("enter to continue........")

        else:
            print("There is no item in cart.....")
            input("enter to continue........")
            continue

    
    elif option =="4":
        system("clear")
        tprint("Purchase History")
        if os.path.exists("receipt.txt"):
            receipt_file = open("receipt.txt", "r")
            line_list = receipt_file.readlines()
            for line in line_list:
                print(line)
            input("enter to continue........")
        else:
            print("There is no history record.....")
            input("enter to continue........")
            continue
    elif option =="5":
        system("clear")
        print("Thanks for purchase.")
        continue
    else:
        print("invalid")
        system("clear")

print("Bye, see you next time!!")