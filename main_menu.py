from os import system
from art import *
import os.path
import json
from functions import *



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

            # select = submenu(origial_dict)
            if select in origial_dict:
                system("clear")
                tprint("Cupecake Menu")
                # buy_item(select)
            
                
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

            # choice = cartmenu(cart_dict)
            if choice == False:
                input("You don't have any items in the shopping cart, press enter to return to main menu....")
                break
            elif choice in cart_dict:
                print("aaaa")
                # delete_item(choice)
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
            # display_receipt(cart_dict)
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