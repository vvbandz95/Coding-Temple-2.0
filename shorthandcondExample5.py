# 5 

current_hour = 15 # integer to represent hour in 25 hour format
hunger_level = 7  # integer on a scale of 1 to 10, 10 is extremely hungry

meal = "snack" if current_hour < 17 and hunger_level < 5 else "full meal"
print(meal)