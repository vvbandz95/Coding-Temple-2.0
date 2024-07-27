# 3 

hour_of_day = 7 # using integer to represent hour in 24- hour format
energy_level = 3 # using integer on a scale of 1 to 5, where 5 is energetic 

beverage = "coffee" if (6 <= hour_of_day < 12) and energy_level < 4 else "tea"
print(beverage) # outputs: coffee
