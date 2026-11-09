import json
import os

# File to store tasks persistently
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file if it exists."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks):
    """Save the current task list to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def todo_list_manager():
    tasks = load_tasks()  # Load tasks when entering the manager
    
    while True:
        print("\n=== To-Do List Manager ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Return to Main Menu")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            if not tasks:
                print("\nYour to-do list is empty.")
            else:
                print("\n--- Your Tasks ---")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                    
        elif choice == '2':
            new_task = input("Enter the task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)  # Save changes immediately
                print(f"Task '{new_task}' added successfully!")
            else:
                print("\n[Warning] Task cannot be empty.")
                
        elif choice == '3':
            if not tasks:
                print("\nYour to-do list is empty.")
            else:
                print("\n--- Your Tasks ---")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                try:
                    task_num = int(input("Enter the task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        save_tasks(tasks)  # Save changes immediately
                        print(f"Task '{removed}' removed successfully!")
                    else:
                        print("\n[Warning] Invalid task number.")
                except ValueError:
                    print("\n[Warning] Please enter a valid number.")
                    
        elif choice == '4':
            print("\nReturning to Main Menu...")
            break
        else:
            print(f"\n[Warning] '{choice}' is not a valid option. Please choose between 1 and 4.")

def simple_calculator():
    # Placeholder for your calculator logic
    print("\n[Simple Calculator placeholder]")

def number_guessing_game():
    # Placeholder for your guessing game logic
    print("\n[Number Guessing Game placeholder]")

# Main Program Loop
def main():
    print("================================")
    print(" Welcome to Your Personal Mini-Toolkit! ")
    print("================================")
    
    while True:
        print("\n=== Personal Mini-Toolkit Menu ===")
        print("1. To-Do List Manager")
        print("2. Simple Calculator")
        print("3. Number Guessing Game")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            todo_list_manager()
        elif choice == '2':
            simple_calculator()
        elif choice == '3':
            number_guessing_game()
        elif choice == '4':
            print("\nThank you for using Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print(f"\n[Warning] '{choice}' is not a valid menu option. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()