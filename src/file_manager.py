import csv
import os
import shutil
from src.expense import Expense

DATA_DIR = "data"
FILE_PATH = "data/expenses.csv"
BACKUP_PATH = "data/expenses_backup.csv"

def ensure_data_folder():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_expenses():
    expenses = []
    if not os.path.exists(FILE_PATH):
        return expenses

    with open(FILE_PATH, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            expenses.append(Expense(row[2], row[1], row[0], row[3]))
    return expenses

def save_expenses(expenses):
    ensure_data_folder()
    with open(FILE_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        for e in expenses:
            writer.writerow(e.to_list())

def backup_data():
    ensure_data_folder()
    if os.path.exists(FILE_PATH):
        shutil.copy(FILE_PATH, BACKUP_PATH)
        print("✅ Backup created successfully")
    else:
        print("❌ No data file to backup")

def restore_data():
    if os.path.exists(BACKUP_PATH):
        shutil.copy(BACKUP_PATH, FILE_PATH)
        print("✅ Data restored from backup")
    else:
        print("❌ No backup file found")
