
print("Welcome to the Habit Tracker!")

habits = []
completed_habits = []

while True:
    print("\nPlease select an option:")
    print("1. Add a new habit!")
    print("2. View your habits!")
    print("3. Mark a habit as completed!")
    print("4. Delete a habit!")
    print("5. Edit a habit!")
    print("6. Exit!")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        habit_name = input("Enter the name of the habit: ")

        if habit_name not in habits:
            habits.append(habit_name)
            print(f"Habit '{habit_name}' added successfully!")
        else:
            print("This habit already exists!")

    elif choice == "2":
        print("\nHere are your habits:")

        if not habits:
            print("No habits found!")
        else:
            for habit in habits:
                if habit in completed_habits:
                    print(f"{habit} - Completed")
                else:
                    print(f"{habit} - Pending")

    elif choice == "3":
        habit_name = input("Enter the name of the habit to mark as completed: ")

        if habit_name in habits:
            if habit_name not in completed_habits:
                completed_habits.append(habit_name)
                print(f"Habit '{habit_name}' marked as completed!")
            else:
                print("This habit is already completed!")
        else:
            print(f"Habit '{habit_name}' not found!")

    elif choice == "4":
        habit_name = input("Enter the name of the habit to delete: ")

        if habit_name in habits:
            habits.remove(habit_name)

            if habit_name in completed_habits:
                completed_habits.remove(habit_name)

            print(f"Habit '{habit_name}' deleted successfully!")
        else:
            print(f"Habit '{habit_name}' not found!")

    elif choice == "5":
        habit_name = input("Enter the name of the habit to edit: ")

        if habit_name in habits:
            new_habit_name = input("Enter the new name for the habit: ")

            index = habits.index(habit_name)
            habits[index] = new_habit_name

            if habit_name in completed_habits:
                completed_habits.remove(habit_name)
                completed_habits.append(new_habit_name)

            print(f"Habit updated to '{new_habit_name}' successfully!")
        else:
            print(f"Habit '{habit_name}' not found!")

    elif choice == "6":
        print("Exiting the Habit Tracker. Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1 and 6.")
