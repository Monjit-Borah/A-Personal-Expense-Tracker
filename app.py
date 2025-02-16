# Smart Expense Tracker in Python

# Import necessary libraries
import json
from datetime import datetime

# File to store expense data
data_file = "expenses.json"

# Function to load existing data
def load_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save data
def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

# Function to add a new expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., food, travel, bills): ")
    amount = float(input("Enter the amount: "))
    note = input("Enter a note (optional): ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }

    data = load_data()
    data.append(expense)
    save_data(data)
    print("Expense added successfully!")

# Function to view expenses
def view_expenses():
    data = load_data()
    if not data:
        print("No expenses found.")
        return

    print("\n--- Expense History ---")
    for expense in data:
        print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Note: {expense['note']}")

# Function to get total expenses
def total_expenses():
    data = load_data()
    total = sum(expense['amount'] for expense in data)
    print(f"\nTotal Expenses: {total}")

# Function to filter expenses by category
def filter_by_category():
    category = input("Enter the category to filter by: ")
    data = load_data()
    filtered = [expense for expense in data if expense['category'].lower() == category.lower()]

    if not filtered:
        print("No expenses found in this category.")
        return

    print(f"\n--- Expenses in {category} ---")
    for expense in filtered:
        print(f"Date: {expense['date']}, Amount: {expense['amount']}, Note: {expense['note']}")


    data = load_data()
    if not data:
        print("No expenses found to export.")
        return

    
# Main menu
def main():
    while True:
        print("\n--- Smart Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Filter by Category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
