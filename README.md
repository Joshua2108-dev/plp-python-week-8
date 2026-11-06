# Personal Mini-Toolkit

## Description
This project is a command-line, menu-driven Python application containing three practical tools:
1. **To-Do List Manager**: Allows users to dynamically view, add, and remove tasks using a Python list.
2. **Simple Calculator**: Performs foundational arithmetic operations with user-friendly formatting and safety error handling.
3. **Number Guessing Game**: An interactive guessing loop utilizing random numbers and conditional hints.

## How to Run It
1. Make sure you have Python installed on your computer.
2. Clone or download this repository.
3. Open your terminal or command prompt in the repository folder.
4. Run the program using the following command:
   ```bash
   python toolkit.py

Reflection
Building this mini-toolkit was a rewarding exercise in bringing variables, loops, conditionals, and data structures together into a single cohesive program. The hardest part for me was structuring the nested loop logic for the To-Do List Manager to make sure users could add and remove items dynamically without breaking the primary menu loop. The bug that took the longest to fix involved handling non-integer inputs gracefully in the calculator and guessing game, which required wrapping inputs inside try-except blocks. With one more week, I would add a persistent file-saving feature using JSON so that user tasks can be saved to disk between sessions.