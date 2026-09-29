# Main Module

from categories import categories
from expenses import add_expense
from summary import show_summary
from menu import show_menu


while True:

    show_menu()

    choice = int(input("Choose an option: "))

    if choice in categories:

        category = categories[choice]

        amount = float(input("Enter expense amount: ₹"))
        description = input("Enter short description: ")

        add_expense(category, amount)

        print("\nExpense added successfully!")

    elif choice == 7:

        show_summary()

    elif choice == 8:

        print("Thank you for using Personal Expense Tracker!")
        break

    else:

        print("Invalid choice! Please try again.")
