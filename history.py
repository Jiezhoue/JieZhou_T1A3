from datetime import datetime

class item:
    def __init__(self, date, item): # initial the class
        self.date = date
        self.item = item

    def add_history(self, date_file, history_dict): # display and save the date of purchase and receipt
        total_amount = 0
        f = open("receipt.txt", "a") # append new receipt in txt file
        dt = datetime.now()
        print(f"Date: {dt}   {dt.strftime('%A')}\n")
        f.write(f"Date: {dt}   {dt.strftime('%A')}\n")
        print("-----------------------------------------\n") # print on the screen
        f.write("-----------------------------------------\n") # save in txt file
        for i in history_dict: # loop all the items in shopping cart when checkout and calculate the total amount
            if i == date_file[dt.strftime('%A')]: # check each item if it's on discount or not based on today's special
                total_amount = total_amount + history_dict[i]['qty'] * (history_dict[i]['price']*(1-0.2))
                print(f"You have purchaced {history_dict[i]['qty']} {history_dict[i]['name']} and price is {history_dict[i]['price']} each\n")
                f.write(f"You have purchaced {history_dict[i]['qty']} {history_dict[i]['name']} and price is {history_dict[i]['price']} each\n")
                print(f"Cause today is {dt.strftime('%A')}, {history_dict[i]['name']} has 20% off\n")
                f.write(f"Cause today is {dt.strftime('%A')}, {history_dict[i]['name']} has 20% off\n")
            else:
                total_amount = total_amount + history_dict[i]['qty'] * history_dict[i]['price']
                print(f"You have purchaced {history_dict[i]['qty']} {history_dict[i]['name']} and price is {history_dict[i]['price']} each\n")
                f.write(f"You have purchaced {history_dict[i]['qty']} {history_dict[i]['name']} and price is {history_dict[i]['price']} each\n")
                
        print(f"total amount is {total_amount}\n")
        f.write(f"total amount is {total_amount}\n")
        print("=============================================================================\n")
        f.write("=============================================================================\n")
        f.close()

    
    

