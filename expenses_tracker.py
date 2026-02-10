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


for k, v in expenses.items():
    print(f"{k}: {v}")