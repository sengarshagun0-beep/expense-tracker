# Summary Module

from expenses import expenses, total_expense


def show_summary():
    print("\n===== EXPENSE SUMMARY =====")

    for category, amount in expenses.items():
        print(category, ": ₹", round(amount, 2))

    print("---------------------------")
    print("Total Expense: ₹", round(total_expense, 2))
