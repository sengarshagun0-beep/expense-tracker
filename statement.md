# Personal Expense Tracker — Project Statement

## 1. Problem Statement

Managing personal expenses manually can make it difficult to keep track of how much money is being spent and where it is being spent.

A user may make several small expenses during the day for food, travel, shopping, education, entertainment, and other purposes. Without organizing these expenses into categories, it can become difficult to understand the overall spending pattern.

The **Personal Expense Tracker** is designed to provide a simple command-line solution for recording and summarizing personal expenses.

The system allows users to select an expense category, enter the amount spent, provide a short description, and view the accumulated expense for each category along with the total expense.

---

## 2. Project Objective

The main objective of this project is to develop a simple Python-based application that allows users to:

* Record personal expenses.
* Categorize expenses.
* Maintain category-wise expense totals.
* Calculate the overall expense.
* View an expense summary.
* Interact with the application through a simple command-line menu.

The project also demonstrates the application of fundamental Python programming concepts to a practical real-world problem.

---

## 3. Scope of the Project

The current scope of the Personal Expense Tracker includes:

### Expense Entry

The user can enter a new expense by selecting one of the predefined categories and providing the amount spent.

### Expense Categories

The system supports the following categories:

1. Food
2. Travel
3. Shopping
4. Education
5. Entertainment
6. Others

### Expense Processing

When an expense is entered, the amount is added to the selected category and to the overall expense total.

### Expense Summary

The user can view the accumulated amount for every category and the total amount spent.

### Program Control

The user can repeatedly add expenses, view the summary, or exit the application through the main menu.

---

## 4. Target Users

The project is intended primarily for:

* Students who want to track daily spending.
* Individuals who want a basic personal expense tracker.
* Beginners learning Python programming.
* Users who need a simple command-line expense recording system.

The application is particularly suitable for users who want a lightweight solution without requiring a complex financial management system.

---

## 5. High-Level Features

### 5.1 Category-Based Expense Entry

Users can select an appropriate category before entering an expense amount.

### 5.2 Expense Amount Recording

The system accepts the amount spent by the user and adds it to the selected category.

### 5.3 Expense Description

Users can enter a short description to provide context for the expense.

### 5.4 Category-Wise Expense Tracking

The application maintains separate totals for:

* Food
* Travel
* Shopping
* Education
* Entertainment
* Others

### 5.5 Total Expense Calculation

All entered expenses are added together to calculate the overall amount spent.

### 5.6 Expense Summary

The summary option displays the current amount spent in each category and the overall total.

### 5.7 Interactive Menu

The application provides a menu-driven interface that allows users to choose what operation they want to perform.

### 5.8 Exit Option

The user can terminate the program using the Exit option.

---

## 6. Functional Modules

Based on the current implementation, the project provides three major functional areas:

### Module 1: Expense Input

This module handles:

* Category selection.
* Expense amount input.
* Expense description input.

### Module 2: Expense Processing

This module:

* Updates the selected category.
* Updates the overall expense.
* Maintains the expense information during program execution.

### Module 3: Expense Summary

This module:

* Displays each expense category.
* Displays category-wise totals.
* Displays the overall total expense.

These modules represent the main user workflow of the application.

---

## 7. Input and Output

### Inputs

The system receives:

* Menu choice from the user.
* Expense amount.
* Short expense description.

### Outputs

The system produces:

* Expense-added confirmation.
* Category-wise expense summary.
* Total expense.
* Invalid-choice message.
* Exit confirmation message.

---

## 8. Basic Workflow

```text
User starts the application
          ↓
Main menu is displayed
          ↓
User selects an option
          ↓
 ┌────────┼───────────────┐
 ↓        ↓               ↓
Add      View            Exit
Expense  Summary
 ↓        ↓               ↓
Select   Display         End
Category Categories
 ↓        + Total
Enter
Amount
 ↓
Enter
Description
 ↓
Update
Expenses
 ↓
Return to
Main Menu
```

---

## 9. Technologies Used

The project is implemented using:

* **Python 3**
* Python dictionaries
* Loops
* Conditional statements
* User input
* Basic arithmetic operations
* Command-line interface

No external Python libraries are required for the current implementation.

---

## 10. Current Project Boundaries

The current version does not include:

* Permanent data storage.
* Database connectivity.
* User login or authentication.
* Expense editing or deletion.
* Graphical user interface.
* Automatic report generation.
* Graphical data visualization.

These features may be considered as future enhancements.

---

## 11. Expected Outcome

The expected outcome of the project is a working command-line application through which a user can record expenses and obtain a simple summary of their spending.

The project demonstrates how basic programming concepts can be combined to create a practical application for personal expense management.

---

## 12. Future Scope

The project can be further developed by adding:

* Persistent storage using files or databases.
* Date and time for every expense.
* Detailed expense history.
* Edit and delete operations.
* Monthly and yearly reports.
* Budget management.
* Spending alerts.
* Data visualization.
* Graphical user interface.
* Modular architecture.
* Automated unit testing.

These enhancements can transform the current basic tracker into a more complete personal finance management application.
