import csv

expenses = {}

with open("expenses.csv", "r") as file:
    data = csv.reader(file)
    next(data)            # Skips the first line (header) in the csv file

    for item in data:
        category = item[0]
        amount = item[1]
        description = item[2]
        expense = (amount, description)

        if category not in expenses.keys():
            expenses[category] = [expense]
        else:
            expenses[category].append(expense)

def view_expenses_for_category(category):
    values = expenses[category]

    print(category.capitalize())
    for price, description in values:
        print(f"{description}: {price}")

    return f"       {category.capitalize()} Total: {get_total_for_category(category)}\n"

def view_all_expenses():
    print()
    for k in expenses.keys():
        print(view_expenses_for_category(k))
        print()

#calclate overall total
def get_total():
    total_spending = 0

    for k in expenses.keys():
        total_spending += get_total_for_category(k)

    print(f"Total spending: {total_spending}")

def get_total_for_category(category):
    total = 0
    values = expenses[category]

    for amount, _ in values:
        total += float(amount)

    return total


def view_categories():
    category = {}
    count = 1
    # print("Select option:")
    for key in expenses.keys():
        print(f"\t{count}: {key.capitalize()}")
        category[(count)] = key
        count += 1

    return category


import csv

def add_expense():
   
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()
    amount = input("Enter price: ").strip()


    new_expense = [category, amount, description]


    with open(expenses.csv, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_expense)

    print("Expense added successfully!")



options = {
    '1': view_all_expenses,
    '2': view_categories,
    '3': get_total,
    '4': add_expense

}


try:
    while True:

        menu = """
            Select option:
                1. View Expense
                2. View Categories
                3. View Total
                4. Add Expense
                5. Exit
            """
        
        print(menu)

        num = input("Select Option: ")

        if num == "5":
            break

        func = options[num]
        func()
        if num == "2":
            op = int(input("Select Option: "))
            category = view_categories
            print(category)
            view_expenses_for_category(category)

except:
    print("ok")
