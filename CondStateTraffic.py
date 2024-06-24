#2 Traffic lights are universal symbols that keep people safe. Each color of the traffic light conveys a specific instruction. Write a program that prompts the user to input the color of a light and output the action a driver should take.

light_color = input("Enter the traffic light color (red, yellow, green):")

if light_color == 'red': 
    print("Stop!")
elif light_color == "yellow": 
    print("Slow down and prepare to stop.")
else: 
    print("Go")
