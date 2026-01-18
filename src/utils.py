from datetime import datetime

def validate_amount(amount):
    if float(amount) <= 0:
        raise ValueError("Amount must be positive")

def validate_date(date_text):
    datetime.strptime(date_text, '%Y-%m-%d')

def pause():
    input("\nPress Enter to continue...")
