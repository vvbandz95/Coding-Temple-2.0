# Example 5 (2.4)

meal_type = input("Do you prefer ver or non- veg?")
dietary_preference = input("Do you want sugar- free or regular?")

if meal_type == "veg":
    if dietary_preference == "sugar-free":
        print("Fruit Salad")
    else:
        print("Veg cake")
else:
    if dietary_preference == "sugar-free":
        print("Sugar- free ice cream!")
    else:
        print("Chocolate Brownie")