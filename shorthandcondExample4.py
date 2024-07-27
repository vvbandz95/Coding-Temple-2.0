#4 

energy_level = 4.5 # using a float on a scale of 1 to 5 where 5 is energetic 
time_availbale = 30.5 # using a float to represent misutes available for workout
short_on_time = time_availbale <45.0

workout = "intense cardio" if energy_level > 4.0 and not short_on_time else "light yoga"
print(workout) # outputs: light yoga 