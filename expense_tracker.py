import calendar
import datetime

from expense import Expense



def main():
    # print a message indicating that the expense tracker is running
    print("Running Expense Tracker")

    # call the get_user_expense function to get expense details from the user
    expense = get_user_expense()
    expense_file_path = "file/expenses.csv"

    # set budget amount
    budget = 7000

    # write user expense to a file
    save_user_expense(expense, expense_file_path)

    # summarize the expenses
    summarize_expense(expense_file_path, budget)


# func for user detail
def get_user_expense():
    print("Getting User Expense")

    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_categories = [
        "Food",
        "Home Bills",
        "Work",
        "Fun",
        "Misc"
    ]

    while True:
        print("Select a Category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        selected_index = int(input("Enter a category number: ")) - 1
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name,
                category=selected_category,
                amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid category, please try again!")


def save_user_expense(expense: Expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expense(expense_file_path, budget):
    print("Summarizing User Expenses")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)

    # group expenses by category
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        amount_by_category[key] = amount_by_category.get(key, 0) + expense.amount

    print("\nExpenses By Category: ")
    for key, amount in amount_by_category.items():
        print(f"{key}: ${amount:.2f}")

    total_spent = sum(x.amount for x in expenses)
    print(f"\nTotal Spent: ${total_spent:.2f}")

    now = datetime.datetime.now()
    remaining_budget = budget - total_spent
    print(f"Budget Remaining: ${remaining_budget:.2f}")

    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    if remaining_days > 0:
        daily_budget = remaining_budget / remaining_days
        print(green(f"Budget Per Day: ${daily_budget:.2f}"))
    else:
        print("End of month reached, no days remaining.")


def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()

