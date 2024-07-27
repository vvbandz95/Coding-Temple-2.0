#Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.


# Function for addition
def add(x, y):
    result = x + y
    print(f"The answer to {x} + {y} is {result}.")
    return result

# Function for subtraction
def subtract(x, y):
    result = x - y
    print(f"The answer to {x} - {y} is {result}.")
    return result

# Function for multiplication
def multiply(x, y):
    result = x * y
    print(f"The answer to {x} * {y} is {result}.")
    return result

# Function for division
def divide(x, y):
    if y == 0:
        print("Error: Division by zero is not allowed.")
        return None
    result = x / y
    print(f"The answer to {x} / {y} is {result}.")
    return result

add(15, 5)
subtract(15, 5)
multiply(15, 5)
divide(15, 5)
divide(15, 0)