# practice creating a dictionary 

friend_1 = {'name': 'joey', 'hobby': 'basketball', 'food': 'pizza'}
friend_2 = {'name': 'kelly', 'hobby': 'ballet', 'food': 'salad'}
friend_3 = {'name': 'valeria', 'hobby': 'writing', 'food': 'sushi'}

print(friend_1['name'])
print(friend_1['hobby'])
print(friend_1['food'])
print(friend_2['name'])
print(friend_2['hobby'])
print(friend_2['food'])
print(friend_3['name'])
print(friend_3['hobby'])
print(friend_3['food'])

# user input
age = input("How old are you?")
age = int(age)
if age <= 12:
    print("\nYou are a child")
elif age <= 18:
    print("\nYou are a teenager")
else:
    print("\nYou are an adult.")

#functions:
def multiply(num1, num2):
    return num1 * num2

def sum_list(numbers):
    return sum(numbers)

result1 = multiply(4, 5)
print("Product:", result1)

result2 = sum_list([1, 2, 3, 4, 5])
print("Sum:", result2) 