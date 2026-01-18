from src.expense import Expense
from src.utils import validate_amount, validate_date, pause
from src.reports import generate_report

def show_menu():
    print("\nPERSONAL FINANCE MANAGER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Generate Report")
    print("4. Backup Data")
    print("5. Restore Data")
    print("6. Exit")


def add_expense(expenses):
    try:
        amount = input("Enter amount: ")
        validate_amount(amount)
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        validate_date(date)
        desc = input("Description: ")
        expenses.append(Expense(amount, category, date, desc))
        print("✅ Expense added")
    except Exception as e:
        print("❌ Error:", e)
    pause()

def view_expenses(expenses):
    for e in expenses:
        print(e)
    pause()

def view_summary(expenses):
    summary = generate_report(expenses)
    for cat, total in summary.items():
        print(f"{cat}: ₹{total:.2f}")
    pause()
