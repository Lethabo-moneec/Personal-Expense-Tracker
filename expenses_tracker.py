import csv

from unicodedata import category

expenses = {}

def read_file():
    with open("expenses.csv", "r") as file:
        data = csv.reader(file)
        next(data)            # Skips the first line (header) in the csv file

        expenses = {}

        for item in data:
            category = item[0]
            amount = item[1]
            description = item[2]
            expense = (amount, description)

            if category not in expenses.keys():
                expenses[category] = [expense]
            else:
                expenses[category].append(expense)
    return expenses


def view_expenses_for_category(category):
    values = expenses[category]

    print(category.capitalize())
    for price, description in values:
        print(f"{description}: {price}")



def view_all_expenses():
    print()
    for k in expenses.keys():
        print(view_expenses_for_category(k))
        print()


#calclate overall total
def get_totals():
    total_spending = 0

    for k in expenses.keys():
        print(f"{k}: {get_total_for_category(k)}")
        total_spending += get_total_for_category(k)

    print(f"Total spending: {total_spending}")


def get_total_for_category(category):
    total = 0
    values = expenses[category]

    for amount, _ in values:
        total += float(amount)

    return total


def add_expense():
   
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()
    amount = int(input("Enter price: ").strip())

    new_expense = [category, amount, description]

    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_expense)

    print("Expense added successfully!")



options = {
    '1': view_all_expenses,
    '2': get_totals,
    '3': add_expense
}


try:
    while True:
        expenses = read_file()

        menu = """
Select option:
    1. View Expense
    2. View Totals
    3. Add Expense
    4. Exit
            """
        
        print(menu)

        num = input("Select Option: ")

        if num == '4':
            break

        func = options[num]
        func()


except:
    print("Please select option")
