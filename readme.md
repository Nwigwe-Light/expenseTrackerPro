💸 Expense Tracker (Python CLI)

A simple command-line expense tracker built with Python.
It lets you record daily expenses, save them to a CSV file, and get budget summaries with per-day spending suggestions.

🚀 Features

Add new expenses with name, amount, and category.

Save expenses to a CSV file (file/expenses.csv).

Summarize spending by category.

Track total spent vs. budget.

Get daily budget recommendations based on remaining days in the month.

Clean, color-coded CLI output. ✅

📂 Project Structure
.
├── expense.py            # Defines the Expense class
├── expense_tracker.py    # Main script (logic for adding/saving/summarizing)
├── file/
│   └── expenses.csv      # CSV file where expenses are stored
└── README.md             # Project documentation

🛠️ Installation & Setup

Clone the repository (or download ZIP):

git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker


Make sure you’re running Python 3.9+:

python --version


Run the app:

python expense_tracker.py

📖 Usage

Run the script.

Enter an expense name.

Enter an amount.

Select a category (Food, Home, Work, Fun, Misc).

The expense will be saved into expenses.csv.

A budget summary will be displayed, including per-day remaining budget.

Example:

Running Expense Tracker
Getting User Expense
Enter expense name: Lunch
Enter expense amount: 12.50
Select a category:
 1. Food
 2. Home
 3. Work
 4. Fun
 5. Misc
Enter a category number [1 - 5]: 1

Saving User Expense: <Expense: Lunch, Food, $12.50> to file\expenses.csv
Summarizing User Expenses

Expenses By Category:
 Food: $12.50

Total Spent: $12.50
Budget Remaining: $6987.50
Budget Per Day: $233.33

📝 Example CSV

file/expenses.csv

Lunch,12.5,Food
Electricity Bill,45.0,Home
Movie Night,20.0,Fun

🎯 Future Improvements

 Add supportfor editing/deleting expenses

 Export summary reports to PDF/Excel

 Add monthly charts with matplotlib

 Make a GUI version (Tkinter or PyQt)

👨‍💻 Author

Built in Python by [Nwigwe-Light]