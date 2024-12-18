#Application that allows users to record and manage their daily expenses. Users can input details such
#as the amount spent, category (e.g., food, transportation, entertainment), and date. The application
#should also allow users to view their spending history, categorize expenses, and generate reports
#summarizing their spending habits. Advanced features might include setting a budget, receiving alerts
#when nearing budget limits, and providing visualizations such as pie charts to represent spending
#distribution.

import json
from datetime import datetime
import matplotlib.pyplot as plt

# File to save data
DATA_FILE = "expenses.json"

# Load data and clear previous expenses
def load_data():
    """Always start with an empty expense list to clear previous data."""
    print("Previous expenses will be cleared as the program starts.")
    data = {"expenses": [], "budget": 0}  # Initialize fresh data
    save_data(data)  # Save the cleared data immediately
    return data


def save_data(data):
    """Save data to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Add a new expense
def add_expense(data):
    """Add an expense to the tracker."""
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category (e.g., food, transport, etc.): ")
    date = input("Enter the date (YYYY-MM-DD, or press Enter for today): ")
    
    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")
    
    expense = {"amount": amount, "category": category, "date": date}
    data["expenses"].append(expense)  # Add expense to list
    save_data(data)  # Save updated data
    print("Expense added successfully!")


# View spending history
def view_history(data):
    """Display all recorded expenses."""
    if len(data["expenses"]) == 0:
        print("No expenses recorded yet.")
        return

    print("\nYour Spending History:")
    for expense in data["expenses"]:
        print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}")


# Categorize expenses
def categorize_expenses(data):
    """Group expenses by category and display totals."""
    category_totals = {}
    
    for expense in data["expenses"]:
        category = expense["category"]
        amount = expense["amount"]
        
        if category not in category_totals:
            category_totals[category] = 0
        
        category_totals[category] += amount
    
    print("\nExpenses by Category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")
    
    return category_totals


# Generate spending report
def generate_report(data):
    """Create a pie chart showing spending distribution."""
    categories = categorize_expenses(data)
    
    if len(categories) == 0:
        print("No expenses to show.")
        return

    labels = list(categories.keys())
    values = list(categories.values())
    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Spending Distribution")
    plt.show()


# Set a budget
def set_budget(data):
    """Set a monthly budget."""
    budget = float(input("Enter your budget for the month: "))
    data["budget"] = budget
    save_data(data)
    print(f"Your budget is set to ${budget:.2f}.")


# Check budget status
def check_budget(data):
    """Check how much of the budget has been spent."""
    total_spent = sum(expense["amount"] for expense in data["expenses"])
    budget = data["budget"]
    
    if budget == 0:
        print("You haven't set a budget yet!")
    elif total_spent >= budget:
        print(f"⚠️ You have exceeded your budget! You spent ${total_spent:.2f}, and your budget is ${budget:.2f}.")
    else:
        print(f"Your spending is under control. You spent ${total_spent:.2f} out of ${budget:.2f}.")


# Main menu
def main():
    """Main program loop."""
    data = load_data()  # Load saved data and clear previous expenses
    
    while True:
        print("\nExpense Manager")
        print("1. Add Expense")
        print("2. View Spending History")
        print("3. Categorize Expenses")
        print("4. Generate Spending Report")
        print("5. Set Budget")
        print("6. Check Budget")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_history(data)
        elif choice == "3":
            categorize_expenses(data)
        elif choice == "4":
            generate_report(data)
        elif choice == "5":
            set_budget(data)
        elif choice == "6":
            check_budget(data)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


# Start the program
if __name__ == "__main__":
    main()

