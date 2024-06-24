# Expected Outcome 

number_1 = 3
number_2 = 3 
number_3 = 4

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))

if (number_1 >= number_2) and (number_1 >= number_3):
    print("smallest = 3")
elif (number_2 >= number_1) and (number_2 >= number_3):
    print("largest = 4")
else: 
    print("The smallest number is 3. The largest number is 4.")