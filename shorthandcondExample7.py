#7 

topic_difficulty = "hard"
available_hours = 3.5 
understanding_level = 6 

study_method = "Deep dive" if topic_difficulty == "hard" and available_hours > 2.5 else "quick review"
bonus_hours = 1.5 if understanding_level < 5 else 0.5 # compund assignment
available_hours += bonus_hours # add bonus hours to available hours 

print(study_method) #outpputs deep dive
print("Total study hours:", available_hours) #outputs: total study hours: 4