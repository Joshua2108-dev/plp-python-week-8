import random

# Tool 1: To-Do List Manager (Uses lists, loops, conditionals, f-strings)
def todo_list_manager():
    tasks = ["Buy groceries", "Finish homework"]
    print("\n--- To-Do List Manager ---")
    
    while True:
        print(f"\nCurrent Tasks ({len(tasks)}):")
        if not tasks:
            print("  (No tasks currently in the list)")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"  {idx}. {task}")
                
        print("\nOptions: [1] Add Task  [2] Remove Task  [3] Back to Main Menu")
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            new_task = input("Enter the task description: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Success: '{new_task}' added to your list.")
            else:
                print("Error: Task description cannot be empty.")
        elif choice == '2':
            if not tasks:
                print("Your list is already empty!")
                continue
            try:
                rem_idx = int(input("Enter the task number to remove: "))
                if 1 <= rem_idx <= len(tasks):
                    removed = tasks.pop(rem_idx - 1)
                    print(f"Success: Removed '{removed}'.")
                else:
                    print("Invalid task number range.")
            except ValueError:
                print("Please enter a valid numeric index.")
        elif choice == '3':
            print("Exiting To-Do List Manager...")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

# Tool 2: Simple Calculator (Uses conditionals and f-strings)
def simple_calculator():
    print("\n--- Simple Calculator ---")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif op == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif op == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print(f"Error: '{op}' is not a valid operator.")
    except ValueError:
        print("Error: Please enter valid numbers.")

# Tool 3: Number Guessing Game (Uses loops, random generation, and conditionals)
def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    secret_number = random.randint(1, 10)
    print("I have picked a number between 1 and 10. Try to guess it!")
    
    while True:
        guess_str = input("Enter your guess (or 'q' to quit): ").strip()
        if guess_str.lower() == 'q':
            print(f"The secret number was {secret_number}.")
            break
        try:
            guess = int(guess_str)
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the secret number {secret_number} correctly!")
                break
        except ValueError:
            print("Please enter a valid integer or 'q' to quit.")

# Main Program Loop
def main():
    print("========================================")
    print("  Welcome to Your Personal Mini-Toolkit! ")
    print("========================================")
    
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