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

    return f"{category.capitalize()} Total: {get_total_for_category(category)}\n"

def view_all_expenses():
    for k in expenses.keys():
        view_expenses_for_category(k)
        print()

def get_total():
    print('getting total')
    total_spending = 0

    for k in expenses.keys():
        total_spending += get_total_for_category(k)

    return total_spending

def get_total_for_category(category):
    total = 0
    values = expenses[category]

    for amount, _ in values:
        total += float(amount)

    return total


def view_categories():
    category = {}
    count = 1
    print("Select option:")
    for key in expenses.keys():
        print(f"\t{count}: {key.capitalize()}")
        category[str(count)] = key
        count += 1

    return category


options = {
    '1': view_all_expenses,
    '2': view_categories,
    '3': get_total
}

menu = """
Select option:
    1. View Expense
    2. Something else
"""

categories = view_categories()
op = input(".")
category = categories[op]
view_expenses_for_category(category)


# try:
#     while True:
#         veiw_options()
#
#         num = int(input("Select Option: "))
#
# except:
#     print("ok")


# print_menu(expenses)
# print(get_totals(expenses))
