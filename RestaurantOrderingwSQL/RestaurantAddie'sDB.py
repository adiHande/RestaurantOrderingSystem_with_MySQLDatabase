import time
import os
from datetime import datetime
import mysql.connector 
MENU_FILENAME = "menu.txt"

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = os.getenv("DB_PASSWORD"),
    database = "restaurant_system"
)

cursor = db.cursor()

# menu = {
#     1: ("Espresso", 3.00),
#     2: ("Americano", 3.50),
#     3: ("Cappuccino", 4.50),
#     4: ("Latte", 4.75),
#     5: ("Matcha Latte", 5.25),
#     6: ("Iced Coffee", 3.75),
#     7: ("Lemonade", 3.50),
#     8: ("Strawberry Lemonade", 4.00),
#     9: ("Blueberry Lemonade", 4.00),
#     10: ("Coke (Fountain)", 2.50),
#     11: ("Zero Coke(Fountain)", 2.50),
#     12: ("Sprite (Fountain)", 2.50),
#     13: ("Orange Juice", 3.25),
#     14: ("Apple Juice", 3.25),
#     15: ("Chocolate Milk", 3.00),
#     16: ("Strawberry Milk", 3.25),
#     17: ("Chickoo Milkshake", 5.50),

    # 18: ("Veggie Burger", 8.99),
    # 19: ("Chicken Burger", 9.99),
    # 20: ("Club Sandwich", 8.49),
    # 21: ("Caprese Sandwich", 8.99),
    # 22: ("Fries", 3.99),
    # 23: ("Peri Peri Fries", 4.49),
    # 24: ("Mozzarella Sticks", 5.99),
    # 25: ("Garlic Knots", 4.99),
    # 26: ("Tater Tots", 4.49),
    # 27: ("Cheese Pizza Slice", 4.00),
    # 28: ("Pepperoni Pizza Slice", 4.50),
    # 29: ("Cheddar Broccoli Soup", 5.99),
    # 30: ("Chicken Noodle Soup", 5.99),
    # 31: ("Pesto Pasta", 10.99),
    # 32: ("Mac n Cheese", 6.99),
    # 33: ("Aglio E Oilio", 12.99),
    # 34: ("Bruschetta", 8.99),
    # 35: ("Ceasar Salad", 7.99),
    # 36: ("Mediterranean Sald", 8.99),
    # 37: ("Burrata", 9.99),

#     38: ("Chocolate Muffin", 3.49),
#     39: ("Blueberry Muffin", 3.49),
#     40: ("New York Cheesecake", 6.99),
#     41: ("Sizzling Brownie w/ Ice Cream", 7.99),
#     42: ("Tiramisu", 6.99),
#     43: ("Honey Castella Cake", 6.49),
#     44: ("Choco Lava Cake", 6.99),
#     45: ("Mochi Donut", 3.99),
#     46: ("Apple Pie", 5.99),
#     47: ("Pumpkin Pie", 6.99),
#     48: ("Pecan Pie", 6.99),
#     49: ("Fruit Cup", 3.49)
# }

def read_menu(filename):
    menu = {}
    sections = []

    with open(filename, "r") as file:
        lines = file.readlines()

    # First non-empty line = sections
    for line in lines:
        if line.strip():  # skip empty lines
            sections = line.strip().split(",")
            break

    # Process item lines
    for line in lines:
        line = line.strip()

        if not line:
            continue  # skip empty lines

        if line[0].isdigit():  # only process lines starting with a number
            parts = line.split(",")
            item_no = int(parts[0])
            section = parts[1]
            name = parts[2]
            price = float(parts[3])

            menu[item_no] = (section, name, price)

    return sections, menu

sections, menu = read_menu(MENU_FILENAME)

def display_menu(sections, menu):
    print("\n")
    print("ADDIE'S MENU".center(50, "༶"))

    for section in sections:
        print("\n" + section.upper().center(50, "‥"))

        for item_no, item in menu.items():
            item_section, name, price = item  # unpack tuple

            if item_section == section:
                print(f"{item_no:>2}. {name:<35} ${price:>6.2f}")

        user_input = input(
            "\nPress Enter for next section or 0 to exit menu: "
        )

        if user_input == "0":
            confirm = input("Done viewing menu? (y/n): ").lower()
            if confirm == "y":
                break

    print("\n" + "༶" * 50)

# def display_menu(sections, menu):
#     print("\n")
#     print("ADDIE'S MENU".center(50, "༶"))
#     print("\n")
#     for section in sections:
#         print("\n" + section.upper().center(50, "‥"))

#         for item_no, item in menu.items():
#             if item["section"] == section:
#                 print(f"{item_no:>2}. {item['name']:<35} ${item['price']:>6.2f}")

#         user_input = input(
#             "\nPress Enter for next section or 0 to exit menu: "
#         )

#         if user_input == "0":
#             confirm = input("Done viewing menu? (y/n): ").lower()
#             if confirm == "y":
#                 break

#     print("\n" + "༶" * 50)



# def display_menu(): #✦
#     print("\n")
#     print("ADDIE'S MENU".center(50, "༶"))
#     print("\n")
#     # -------- DRINKS --------
#     print("DRINKS".center(50, "‥"))
#     for key in range(1, 18):
#         name, price = menu[key]
#         print(f"{key:>2}. {name:<35} ${price:>6.2f}")

#     input("\nPress Enter to view Mains...\n")

#     # -------- MAINS --------
#     print("MAINS".center(50, "‥"))
#     for key in range(18, 38):
#         name, price = menu[key]
#         print(f"{key:>2}. {name:<35} ${price:>6.2f}")

#     input("\nPress Enter to view Desserts...\n")

#     # -------- DESSERTS --------
#     print("DESSERTS".center(50, "‥"))
#     for key in range(38, 50):
#         name, price = menu[key]
#         print(f"{key:>2}. {name:<35} ${price:>6.2f}")

#     print("༶" * 50)

    # for key in menu:
    #     name, price = menu[key]
    #     print(f"{key:>2}. {name:<35} ${price:>6.2f}")

    #     if key == 22:
    #         print("\n--- Press Enter to see more ---")
    #         input()
    #         os.system('cls' if os.name == 'nt' else 'clear')
    #         print("ADDIE'S MENU (continued)".center(50, "-"))

    # print("-" * 50)

order = []

# def customer_order_taking():
#     while True:
#         try:
#             choice = int(input("Enter item number (1-49) or 0 to finish: "))

#             if choice == 0:
#                 if len(order) == 0:
#                     print("\nYou didn’t order anything.")
#                     print(closing_greeting(time_of_day))
#                     exit()   # ← exits entire program
#                 else:
#                     print("Finished ordering.\n")
#                     break

#             if choice not in menu:
#                 print("Invalid item number.\n")
#                 continue

#             quantity = int(input("Enter quantity: "))

#             if quantity <= 0:
#                 print("Quantity must be positive.\n")
#                 continue

#             name, price = menu[choice]
#             order.append((name, quantity, price))
#             print(f"Added {quantity} x {name}\n")

#         except ValueError:
#             print("Please enter a valid number.\n")

def customer_order_taking(menu):
    while True:
        print("\nEnter item number to add.")
        print("Enter 0 when finished.\n")

        try:
            choice = int(input("Item number: "))

            if choice == 0:
                if not order:
                    print("\nYou haven’t ordered anything.")
                    continue

                # Ask to confirm order
                if confirm_order(menu):
                    break
                else:
                    modify_order(menu)
                    continue

            if choice not in menu:
                print("Invalid item number.\n")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be positive.\n")
                continue

            section, name, price = menu[choice]

            order.append((name, quantity, price))
            print(f"Added {quantity} x {name}")

        except ValueError:
            print("Please enter valid numbers.\n")

def confirm_order(menu):
    print("\nYour Current Order:")
    print("-" * 30)

    for idx, (name, qty, price) in enumerate(order, start=1):
        print(f"{idx}. {name} x{qty}")

    print("-" * 30)

    while True:
        confirm = input("Is this correct? (y/n): ").lower()

        if confirm == "y":
            return True
        elif confirm == "n":
            return False
        else:
            print("Please enter y or n.")

def modify_order(menu):
    while True:
        print("\nModify Order Options:")
        print("1. Remove Item")
        print("2. Update Quantity")
        print("3. Add More Items")
        print("0. Done Modifying")

        choice = input("Choose option: ")

        if choice == "1":
            remove_item()

        elif choice == "2":
            update_quantity()

        elif choice == "3":
            return  # go back to adding items

        elif choice == "0":
            return

        else:
            print("Invalid option.")

def remove_item():
    if not order:
        print("Order is empty.")
        return

    for idx, (name, qty, price) in enumerate(order, start=1):
        print(f"{idx}. {name} x{qty}")

    try:
        remove_index = int(input("Enter number to remove: "))
        if 1 <= remove_index <= len(order):
            removed = order.pop(remove_index - 1)
            print(f"Removed {removed[0]}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Enter a valid number.")

def update_quantity():
    if not order:
        print("Order is empty.")
        return

    for idx, (name, qty, price) in enumerate(order, start=1):
        print(f"{idx}. {name} x{qty}")

    try:
        update_index = int(input("Enter number to update: "))

        if 1 <= update_index <= len(order):
            new_qty = int(input("Enter new quantity: "))

            if new_qty <= 0:
                print("Quantity must be positive.")
                return

            name, _, price = order[update_index - 1]
            order[update_index - 1] = (name, new_qty, price)
            print("Quantity updated.")

        else:
            print("Invalid selection.")

    except ValueError:
        print("Enter valid numbers.")



def calculate_totals(order):
    subtotal = 0
    for name, qty, price in order:
        subtotal += qty * price

    tax = subtotal * 0.08
    total_before_tip = subtotal + tax

    return subtotal, tax, total_before_tip


def create_order_in_db(subtotal, tax, total_before_tip):
    insert_query = """
    INSERT INTO orders (subtotal, tax, tip, total, signature)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    cursor.execute(insert_query, (subtotal, tax, 0, total_before_tip, None))
    db.commit()

    order_id = cursor.lastrowid

    cursor.execute("SELECT order_time FROM orders WHERE order_id = %s", (order_id,))
    order_time = cursor.fetchone()[0]

    return order_id, order_time


def insert_order_items(order_id, order):
    insert_item_query = """
    INSERT INTO order_items (order_id, item_name, quantity, price)
    VALUES (%s, %s, %s, %s)
    """

    for name, qty, price in order:
        cursor.execute(insert_item_query, (order_id, name, qty, price))

    db.commit()


# def print_receipt(order_id, order_time, subtotal, tax, total_before_tip):  #print_Bill
#     WIDTH = 50
#     INNER_WIDTH = WIDTH - 2  # space inside | |
#     print("\n")
#     print("-" * WIDTH)
#     # RECEIPT header inside borders
#     print(f"|{'BILL'.center(INNER_WIDTH)}|")
#     print("|" + " " * INNER_WIDTH + "|")

#     order_line = f"Order No: {order_id}"
#     print(f"|{order_line.center(INNER_WIDTH)}|")

#     formatted_time = order_time.strftime("%b %d, %Y  %I:%M %p")
#     date_line = f"{formatted_time}"
#     print(f"|{date_line.center(INNER_WIDTH)}|")

#     print("|" + " " * INNER_WIDTH + "|")  # blank line instead of dashes
#     print("|" + " " * INNER_WIDTH + "|")
#     print("|" + " " * INNER_WIDTH + "|")
#     subtotal = 0

#     for name, qty, price in order:
#         total_price = qty * price
    #     # subtotal += total_price

    #     item_line = f"{name:<29} x{qty:<3} ${total_price:>7.2f}"
    #     print(f"|{item_line.center(INNER_WIDTH)}|")

    # print("|" + " " * INNER_WIDTH + "|")
    # print("|" + " " * INNER_WIDTH + "|")
    # # tax = subtotal * 0.08

    # tax_line = f"Tax (8%): ${tax:.2f}"
    # subtotal_line = f"Subtotal: ${subtotal:.2f}"

    # print(f"|{tax_line.rjust(INNER_WIDTH, '.')}|")
    # print(f"|{subtotal_line.rjust(INNER_WIDTH, '.')}|")

    # print("|" + " " * INNER_WIDTH + "|")

    # # grand_total = subtotal + tax  

    # # tip_line = f"Tip: ${tip:.2f}"
    # print("|" + " " * INNER_WIDTH + "|")
    # print("|" + " " * INNER_WIDTH + "|")
    # print("|" + " " * INNER_WIDTH + "|")
    # total_line = f"Total: ${total_before_tip:.2f}"

    # # print(f"|{tip_line.rjust(INNER_WIDTH, '.')}|")
    # print(f"|{total_line.rjust(INNER_WIDTH, '.')}|")

    # print("|" + " " * INNER_WIDTH + "|")  # blank line before thank you
    # print("|" + " " * INNER_WIDTH + "|")
    # print("|" + " " * INNER_WIDTH + "|")
    # print("|" + " " * INNER_WIDTH + "|")
    # print("|" + " " * INNER_WIDTH + "|")
    # print("|" + " " * INNER_WIDTH + "|")
    # print("|" + " " * INNER_WIDTH + "|")
    # print("|" + " " * INNER_WIDTH + "|")
    # # THANK YOU inside borders
    # print(f"|{'Thank You!'.center(INNER_WIDTH)}|")

    # print("-" * WIDTH)

def print_receipt(order_id, order_time, subtotal, tax, total_before_tip):
    WIDTH = 50
    INNER_WIDTH = WIDTH - 2

    print("\n" + "-" * WIDTH)

    print(f"|{'BILL'.center(INNER_WIDTH)}|")
    print("|" + " " * INNER_WIDTH + "|")

    print(f"|{f'Order No: {order_id}'.center(INNER_WIDTH)}|")

    formatted_time = order_time.strftime("%b %d, %Y  %I:%M %p")
    print(f"|{formatted_time.center(INNER_WIDTH)}|")

    print("|" + " " * INNER_WIDTH + "|")

    for name, qty, price in order:
        total_price = qty * price
        item_line = f"{name:<29} x{qty:<3} ${total_price:>7.2f}"
        print(f"|{item_line.center(INNER_WIDTH)}|")

    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    print(f"|{f'Tax (8%): ${tax:.2f}'.rjust(INNER_WIDTH, '.')}|")
    print(f"|{f'Subtotal: ${subtotal:.2f}'.rjust(INNER_WIDTH, '.')}|")

    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    print(f"|{f'Total: ${total_before_tip:.2f}'.rjust(INNER_WIDTH, '.')}|")

    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    print(f"|{'Thank You!'.center(INNER_WIDTH)}|")

    print("-" * WIDTH)


def update_order_with_tip(order_id, tip, signature):
    cursor.execute("""
        UPDATE orders
        SET tip = %s,
            total = subtotal + tax + %s,
            signature = %s
        WHERE order_id = %s
    """, (tip, tip, signature, order_id))

    db.commit()

# def recpt_after_tip(order_id, order_time, subtotal, tax, total_before_tip, tip, signature):
#     # subtotal = 0
#     # total_price = 0 
#     # for name, qty, price in order:
#     #     total_price = qty * price
#     #     subtotal += total_price
#     # tax = subtotal * 0.08
#     grand_total = total_before_tip + tip
#     WIDTH = 50
#     INNER_WIDTH = WIDTH - 2
#     print("\n")
#     print("-" * WIDTH)

#     print(f"|{'RECEIPT'.center(INNER_WIDTH)}|")
#     print("|" + " " * INNER_WIDTH + "|")

#     order_line = f"Order No: {order_id}"
#     print(f"|{order_line.center(INNER_WIDTH)}|")

#     formatted_time = order_time.strftime("%b %d, %Y  %I:%M %p")
#     date_line = f"{formatted_time}"
#     print(f"|{date_line.center(INNER_WIDTH)}|")
#     # print(f"|{'Date: {order_time}'.center(INNER_WIDTH)}|")
#     print("|" + " " * INNER_WIDTH + "|")
#     print("|" + " " * INNER_WIDTH + "|")
#     print("|" + " " * INNER_WIDTH + "|")

#     # subtotal = 0
#     # total_price = 0
#     for name, qty, price in order:
#         total_price = qty * price
#         # subtotal += total_price
#         item_line = f"{name:<29} x{qty:<3} ${total_price:>7.2f}"
#         print(f"|{item_line.center(INNER_WIDTH)}|")

#     print("|" + " " * INNER_WIDTH + "|")
#     print("|" + " " * INNER_WIDTH + "|")

#     # tax = subtotal * 0.08
#     subtotal_line = f"Subtotal: ${subtotal:.2f}"
#     tax_line = f"Tax (8%): ${tax:.2f}"

#     print(f"|{tax_line.rjust(INNER_WIDTH, '.')}|")
#     print(f"|{subtotal_line.rjust(INNER_WIDTH, '.')}|")

#     # grand_total = subtotal + tax + tip

#     print("|" + " " * INNER_WIDTH + "|")
#     print("|" + " " * INNER_WIDTH + "|")
#     print("|" + " " * INNER_WIDTH + "|")

#     total_line = f"Total: ${grand_total:.2f}"
#     print(f"|{total_line.rjust(INNER_WIDTH, '.')}|")

#     print("|" + " " * INNER_WIDTH + "|")
#     print("|" + " " * INNER_WIDTH + "|")
#     print("|" + " " * INNER_WIDTH + "|")
#     print("|" + " " * INNER_WIDTH + "|")
#     print("|" + " " * INNER_WIDTH + "|")
#     print("|" + " " * INNER_WIDTH + "|")

#     # SIGNED LINE RIGHT BEFORE THANK YOU
#     signed_line = f"____ Tip: ${tip:.2f} ____ Sign here: {signature} ____"
#     print(f"|{signed_line.center(INNER_WIDTH)}|")

#     print("|" + " " * INNER_WIDTH + "|")

#     print(f"|{'Thank You!'.center(INNER_WIDTH)}|")

#     print("-" * WIDTH)

def recpt_after_tip(order_id, order_time, subtotal, tax, total_before_tip, tip, signature):
    grand_total = total_before_tip + tip

    WIDTH = 50
    INNER_WIDTH = WIDTH - 2

    print("\n" + "-" * WIDTH)

    print(f"|{'RECEIPT'.center(INNER_WIDTH)}|")
    print("|" + " " * INNER_WIDTH + "|")

    print(f"|{f'Order No: {order_id}'.center(INNER_WIDTH)}|")

    formatted_time = order_time.strftime("%b %d, %Y  %I:%M %p")
    print(f"|{formatted_time.center(INNER_WIDTH)}|")

    print("|" + " " * INNER_WIDTH + "|")

    for name, qty, price in order:
        total_price = qty * price
        item_line = f"{name:<29} x{qty:<3} ${total_price:>7.2f}"
        print(f"|{item_line.center(INNER_WIDTH)}|")

    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    print(f"|{f'Tax (8%): ${tax:.2f}'.rjust(INNER_WIDTH, '.')}|")
    print(f"|{f'Subtotal: ${subtotal:.2f}'.rjust(INNER_WIDTH, '.')}|")

    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    print(f"|{f'Total: ${grand_total:.2f}'.rjust(INNER_WIDTH, '.')}|")

    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    print("|" + " " * INNER_WIDTH + "|")
    signed_line = f"____ Tip: ${tip:.2f} ____ Sign: {signature} ____"
    print(f"|{signed_line.center(INNER_WIDTH)}|")

    print("|" + " " * INNER_WIDTH + "|")

    print(f"|{'Payment Approved ✓'.center(INNER_WIDTH)}|")
    print(f"|{'Thank You!'.center(INNER_WIDTH)}|")

    print("-" * WIDTH)

def get_time_of_day(hour):    
    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    elif 17 <= hour < 21:
        return "evening"
    else:
        return "night"

current_hour = datetime.now().hour     
time_of_day = get_time_of_day(current_hour)

def closing_greeting(time_of_day):
    if time_of_day in ["morning", "afternoon"]:
        return "Have a good day!"
    elif time_of_day == "evening":
        return "Have a good rest of your evening!"
    elif time_of_day == "night":
        return "Good night!"
    else:
        return "Bye bye!"

print("\n")
print("  ADDIE'S  ".center(120, '=')) 
print("\n\nHello! Welcome to Addie's\n")
time.sleep(1)
print(" Here's your menu")
time.sleep(2)
display_menu(sections, menu)
time.sleep(1)
print("\nWhat would you like to order today?\n")
# print("Enter '0' when you're done ordering")
time.sleep(1)
customer_order_taking(menu)
print("\nI'll bring your order when it's ready \n")
time.sleep(6)
print("\nHere is your order")
print("\nEnjoy!\n\n")
time.sleep(2)
bill_input = input("\nType 'bill' when you're ready for your bill:\n").lower()

while bill_input != "bill":
    bill_input = input("Please type 'bill' to receive your bill:\n").lower()

subtotal, tax, total_before_tip = calculate_totals(order)
order_id, order_time = create_order_in_db(subtotal, tax, total_before_tip)
insert_order_items(order_id, order)

print_receipt(order_id, order_time, subtotal, tax, total_before_tip)
# print_receipt()

tip = float(input("\nEnter tip amount (0 if none): $"))
signature = input("Sign here (initials): ")

update_order_with_tip(order_id, tip, signature)

recpt_after_tip(order_id, order_time, subtotal, tax, total_before_tip, tip, signature)
# recpt_after_tip(tip, signature)

time.sleep(2)
print("\n\n\nThank you for visiting Addie's!\n")
time.sleep(2)
print(closing_greeting(time_of_day))
