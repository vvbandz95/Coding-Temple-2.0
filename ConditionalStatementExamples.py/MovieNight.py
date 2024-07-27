# 2.4 Python examples Exercise 1 *hint* Use nested 'if' statements to determine the movie genre based on the user's mood and the day's weather 

mood = input("How are you feeling today? (happy, sad, adventurous): ")
weather = input("What's the weather like? (sunny/rainy): ")


if mood == "happy":
    if weather == "sunny":
        print("Comedy")
    else:
        print("Romantic")
elif mood == "sad":
    print("Drama")
else:
    print("Adventure")