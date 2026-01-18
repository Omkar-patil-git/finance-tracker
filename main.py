from src.file_manager import (
    load_expenses, save_expenses,
    backup_data, restore_data
)
from src.menu import show_menu, add_expense, view_expenses
from src.reports import generate_report

expenses = load_expenses()

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_expense(expenses)
        save_expenses(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        generate_report(expenses)

    elif choice == "4":
        backup_data()

    elif choice == "5":
        restore_data()
        expenses = load_expenses()

    elif choice == "6":
        save_expenses(expenses)
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
