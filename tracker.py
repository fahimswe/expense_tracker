import csv
from datetime import datetime

FILENAME = 'expenses.csv'

def load_expenses():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)

def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    expenses.append({
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    })

    save_expenses(expenses)
    print("✅ Expense added successfully.\n")

def view_expenses(expenses):
    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | ${exp['amount']} | {exp['description']}")

def total_by_category(expenses):
    category = input("Enter category: ")
    total = sum(float(exp['amount']) for exp in expenses if exp['category'] == category)
    print(f"💰 Total spent in '{category}': ${total:.2f}")

def menu():
    expenses = load_expenses()
    while True:
        print("\n---- Expense Tracker ----")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total by Category")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            total_by_category(expenses)
        elif choice == '4':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    menu()
