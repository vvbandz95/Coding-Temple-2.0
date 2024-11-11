# even or odd 1.1
# apparently this was not correct for this exercise. Can you help me understand why I wouldn't write the code like this but would write it the following way 
number = int(input("Enter a number, and I'll tell you if it's even or odd:"))
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.") 
else:
    print("\nThe number " + str(number) + " is odd.")

# even or odd, correct way 1.2
def even_or_odd(number):

    if number % 2 == 0:
        return "Even"
    else: 
        return "Odd"
    
# convert a number to a string 
def number_to_string(number):
    # Return a string of the number here!
    number_str = str(number)
    return str(number)

# vowel count
def get_count(sentence):
    pass
    vowels = "aeiou"
    return sum(1 for char in sentence if char in vowels)
    
input_string = "hello coding temple"
print(get_count(input_string))  