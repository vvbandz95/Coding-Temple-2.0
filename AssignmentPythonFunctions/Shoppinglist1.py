# Task 2.1: Write a function that lets the user add items to a list.

def add_item(shopping_list, item):
    "Adds an item to the shopping list."
    shopping_list.append(item)
    print(f"Added '{item}' to the list.")

def remove_item(shopping_list, item):
    "Removes an item from the shopping list."
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed '{item}' from the list.")
    else:
        print(f"'{item}' not found in the list.")

def print_list(shopping_list):
    "Prints the shopping list in a simple way."
    if shopping_list:
        print("\nShopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
        print() 
    else:
        print("\nShopping list is empty.\n")

def shopping_list_program():
    "Run the shopping list."
    shopping_list = []  
    print("Welcome to the Shopping List!")
    
    while True:
        print("\nOptions:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Print the list")
        print("4. Quit")

        choice = input("Choose a number: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Exiting the Shopping List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

shopping_list_program()
