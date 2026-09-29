# Personal Expense Tracker

## Overview

**Personal Expense Tracker** is a simple command-line Python application designed to help users record and monitor their daily expenses.

The application allows users to select an expense category, enter the amount spent, provide a short description, and view a summary of their total expenses. It organizes expenses into predefined categories such as Food, Travel, Shopping, Education, Entertainment, and Others.

The project demonstrates basic Python programming concepts including dictionaries, loops, conditional statements, user input, type conversion, and basic data processing.

---

## Features

The Personal Expense Tracker provides the following features:

### 1. Add an Expense

Users can add a new expense by:

* Selecting an expense category.
* Entering the expense amount.
* Entering a short description of the expense.

Available categories are:

* Food
* Travel
* Shopping
* Education
* Entertainment
* Others

### 2. Expense Categorization

Every expense is assigned to one of the predefined categories. The program maintains a separate total for each category.

For example:

```text
Food: ₹500
Travel: ₹300
Shopping: ₹700
```

### 3. View Expense Summary

Users can select **View Summary** to see:

* Total amount spent in each category.
* Overall total expense.

The amounts are displayed up to two decimal places.

### 4. Exit the Application

Users can choose the **Exit** option to safely terminate the program.

---

## Project Workflow

The basic workflow of the application is:

```text
Start
  ↓
Display Main Menu
  ↓
Select an Option
  ↓
 ┌───────────────────────┐
 │                       │
Add Expense        View Summary
 │                       │
 ↓                       ↓
Select Category     Display Category
 │                   Expenses
 ↓                       │
Enter Amount              ↓
 │                  Display Total
 ↓                       │
Enter Description         │
 │                       │
 ↓                       │
Update Expense Total      │
 │                       │
 └───────────┬───────────┘
             ↓
       Display Main Menu
             ↓
          Exit?
          /   \
        No     Yes
        ↓       ↓
      Menu     End
```

---

## Technologies Used

* **Python 3**
* Python built-in data structures
* Command Line / Terminal
* Git and GitHub for version control and project submission

### Python Concepts Used

The project uses:

* Variables
* Dictionaries
* `while` loop
* `for` loop
* `if-elif-else` statements
* User input using `input()`
* Type conversion using `int()` and `float()`
* Dictionary operations
* Functions are not currently used in this version
* Basic numerical calculations
* Formatted console output

---

## Project Structure

The current project is a simple Python console application.

```text
Personal-Expense-Tracker/
│
├── expense_tracker.py
├── README.md
└── statement.md
```

### File Description

| File                 | Description                                                             |
| -------------------- | ----------------------------------------------------------------------- |
| `expense_tracker.py` | Main Python program containing the expense tracker implementation       |
| `README.md`          | Project documentation, setup, features, and usage instructions          |
| `statement.md`       | Problem statement, project scope, target users, and high-level features |

---

## Installation

### Step 1: Install Python

Download and install Python 3 from the official Python website if it is not already installed.

During installation on Windows, make sure the option to add Python to the system PATH is enabled.

### Step 2: Download or Clone the Project

Clone the GitHub repository or download the project files to your computer.

### Step 3: Open the Project Folder

Open Command Prompt, PowerShell, or a terminal inside the project folder.

---

## How to Run

Run the following command:

```bash
python expense_tracker.py
```

If your system uses `python3`, use:

```bash
python3 expense_tracker.py
```

The main menu will appear in the terminal.

---

## How to Use

When the program starts, the following menu is displayed:

```text
===== PERSONAL EXPENSE TRACKER =====
1. Food
2. Travel
3. Shopping
4. Education
5. Entertainment
6. Others
7. View Summary
8. Exit
```

### Adding an Expense

Suppose you spent ₹250 on lunch.

Select:

```text
Choose an option: 1
```

The program will ask:

```text
Enter expense amount: ₹250
Enter short description: Lunch
```

The expense will then be added to the **Food** category.

### Viewing the Summary

Select:

```text
Choose an option: 7
```

The program displays the amount recorded for every category and the overall total.

Example:

```text
===== EXPENSE SUMMARY =====
Food : ₹ 250.0
Travel : ₹ 0.0
Shopping : ₹ 500.0
Education : ₹ 0.0
Entertainment : ₹ 150.0
Others : ₹ 0.0
---------------------------
Total Expense: ₹ 900.0
```

### Exiting

Select:

```text
Choose an option: 8
```

The application will display a thank-you message and terminate.

---

## Input and Output

### Input

The program accepts:

1. Menu option
2. Expense amount
3. Short description

Example:

```text
Choose an option: 3
Enter expense amount: ₹500
Enter short description: New notebook
```

### Output

The program provides:

* Confirmation when an expense is added.
* Expense summary by category.
* Total expense.
* Error message when an invalid menu option is entered.

---

## Testing

The application can be tested manually through the command line.

### Test Case 1: Add Food Expense

**Input:**

```text
1
250
Lunch
```

**Expected Result:**

```text
Expense added successfully!
```

The Food category should increase by ₹250.

### Test Case 2: Add Multiple Expenses

Add expenses under different categories.

**Expected Result:**

Each category should maintain its own total and the overall total should contain the sum of all entered expenses.

### Test Case 3: View Summary

Select:

```text
7
```

**Expected Result:**

The program should display all categories and their current totals along with the total expense.

### Test Case 4: Invalid Menu Option

Enter an option outside the available choices, such as:

```text
10
```

**Expected Result:**

```text
Invalid choice! Please try again.
```

### Test Case 5: Exit

Select:

```text
8
```

**Expected Result:**

```text
Thank you for using Personal Expense Tracker!
```

---

## Current Limitations

The current version is intentionally simple and has some limitations:

* Expenses are stored only while the program is running.
* Data is not saved to a file or database.
* The description is accepted but is not displayed in the summary.
* There is no option to edit or delete an expense.
* There is no graphical user interface.
* Input validation for non-numeric values is limited.
* The current implementation is contained in a single Python source file.

---

## Future Enhancements

The project can be extended with:

* Saving expenses permanently using CSV or JSON.
* Database integration using SQLite.
* Separate expense records with date and description.
* Edit and delete functionality.
* Monthly and weekly expense reports.
* Graphs and charts for expense analysis.
* Budget limits and alerts.
* Better input validation and exception handling.
* A graphical user interface.
* Modular Python files and functions.
* Automated testing.

---

## Conclusion

The Personal Expense Tracker provides a simple way to record and summarize personal expenses through a command-line interface.

The project applies fundamental Python programming concepts to a practical real-world problem and provides a foundation that can be expanded into a more advanced expense management system.
