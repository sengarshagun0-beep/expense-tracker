# Expenses Module

expenses = {
    "Food": 0,
    "Travel": 0,
    "Shopping": 0,
    "Education": 0,
    "Entertainment": 0,
    "Others": 0
}

total_expense = 0


def add_expense(category, amount):
    global total_expense

    expenses[category] += amount
    total_expense += amount
