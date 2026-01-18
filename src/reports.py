from collections import defaultdict

def calculate_totals(expenses):
    total = sum(e.amount for e in expenses)
    average = total / len(expenses) if expenses else 0
    return total, average

def category_wise_expenses(expenses):
    categories = defaultdict(float)
    for e in expenses:
        categories[e.category] += e.amount
    return categories

def generate_report(expenses):
    total, average = calculate_totals(expenses)
    categories = category_wise_expenses(expenses)

    print("\n========== EXPENSE REPORT ==========")
    print(f"Total Expenses   : ₹{total:.2f}")
    print(f"Average Expense : ₹{average:.2f}")
    print("\nCategory-wise Breakdown:")
    for cat, amt in categories.items():
        print(f"  {cat}: ₹{amt:.2f}")
    print("===================================")
