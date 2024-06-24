#3 Task 2.2 the smallest

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))

if (number_1 <= number_2) and (number_1 <= number_3):
    print("smallest = 5")
elif (number_2 <= number_1) and (number_2 <= number_3):
    print("smallest = 7")
else: 
    print("smallest = 6")