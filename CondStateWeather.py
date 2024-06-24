#1 Weather plays a pivotal role in our daily wardrobe choices. As temps fluctuate, so do our needs for layers, jackets, or light clothing. Based on the temp entered by the user, suggest an outfit to wear 

temperature = float(input("Enter today's temperature in Fahrenheit: "))

if temperature < 20: 
    print("Wear a heavy coat and scarf!")
elif 20 <= temperature <= 50: 
    print("It is a little chilly. Make sure to wear a light coat")
elif 51 <= temperature <= 70: 
    print("It might be a good idea to wear a t- shirt and some long pants")
else:
    print("It feels great! This is t- shirt weather!")


