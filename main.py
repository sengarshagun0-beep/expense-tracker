# Main Module

# Personal Expense Tracker

expenses = {
    "Food": 0,
    "Travel": 0,
    "Shopping": 0,
    "Education": 0,
    "Entertainment": 0,
    "Others": 0
}

total_expense = 0

while True:
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Food")
    print("2. Travel")
    print("3. Shopping")
    print("4. Education")
    print("5. Entertainment")
    print("6. Others")
    print("7. View Summary")
    print("8. Exit")

    choice = int(input("Choose an option: "))

    categories = {
        1: "Food",
        2: "Travel",
        3: "Shopping",
        4: "Education",
        5: "Entertainment",
        6: "Others"
    }

    if choice in categories:
        category = categories[choice]

        amount = float(input("Enter expense amount: ₹"))
        description = input("Enter short description: ")

        expenses[category] += amount
        total_expense += amount

        print("\nExpense added successfully!")

    elif choice == 7:
        print("\n===== EXPENSE SUMMARY =====")

        for category, amount in expenses.items():
            print(category, ": ₹", round(amount, 2))

        print("---------------------------")
        print("Total Expense: ₹", round(total_expense, 2))

    elif choice == 8:
        print("Thank you for using Personal Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")

        
