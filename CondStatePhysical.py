#5 Physical activityt is a cornerstone of a healthy lifestyle, offering benefits form improved heart health to mental wellbeing. Health experts recommend certain daily activity levels/ benchmarks for optimal health. Ask the user how many minutes they exercis daily to provicde health advice. 

exercise_minutes = int(input("How many minutes do you exercise daily?"))

if exercise_minutes < 30: 
    print("You should consider exercising more for better health!")
elif 30 <= exercise_minutes <= 60: 
    print("Great job staying active!")
else: 
    print("You're an exercise superstar!")