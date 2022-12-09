from datetime import datetime

class item:
    def __init__(self, date, item):
        self.date = date
        self.item = item

    def add_history(self, date_file, history_dict):
        total_amount = 0
        f = open("receipt.txt", "a")
        dt = datetime.now()
        print(f"Date: {dt}   {dt.strftime('%A')}\n")
        f.write(f"Date: {dt}   {dt.strftime('%A')}\n")
        print("-----------------------------------------\n")
        f.write("-----------------------------------------\n") 
        for i in history_dict:
            if i == date_file[dt.strftime('%A')]:
                total_amount = total_amount + history_dict[i]['qty'] * (history_dict[i]['price']*(1-0.2))
                print(f"You have purchaced {history_dict[i]['qty']} {history_dict[i]['name']} and price is {history_dict[i]['price']} each\n")
                f.write(f"You have purchaced {history_dict[i]['qty']} {history_dict[i]['name']} and price is {history_dict[i]['price']} each\n")
                print(f"Cause today is {dt.strftime('%A')}, this item can have 20% off\n")
                f.write(f"Cause today is {dt.strftime('%A')}, this item can have 20% off\n")
                print(f"total amount is {total_amount}\n")
                f.write(f"total amount is {total_amount}\n")
            else:
                total_amount = total_amount + history_dict[i]['qty'] * history_dict[i]['price']
                print(f"You have purchaced {history_dict[i]['qty']} {history_dict[i]['name']} and price is {history_dict[i]['price']} each\n")
                f.write(f"You have purchaced {history_dict[i]['qty']} {history_dict[i]['name']} and price is {history_dict[i]['price']} each\n")
                print(f"total amount is {total_amount}\n")
                f.write(f"total amount is {total_amount}\n")
        print("=============================================================================\n")
        f.write("=============================================================================\n")
        f.close()

    
    

