print("Welcome to the Daily Expense Tracker!")
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
expenses = []
while True:
    choice = input()

    if choice == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break

    elif choice == "1" :
        expense = float(input())
        expenses.append(expense)
        print("Expense added successfully!")
    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i, expense in enumerate(expenses, 1):
                print(f"{i}. {expense}")
    elif choice == "3" :
        if not expenses :
            print("No expenses recorded yet.")
        else :
            total = 0
            for i, expense in enumerate(expenses,0):
                total += expense
            print(f"Total expense: {total}")
            count_expenses = len(expenses)
            average = total /count_expenses
            print(f"Average expense: {average}")
    elif choice == "4":
        expenses = []
        print("All expenses cleared.")
    else :
        print("Invalid choice. Please try again.")
      
