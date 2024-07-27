# 2.4 Example 2, temperature 

temperature = float(input("What's the temp today in Fahrenheit? "))
event_type = input("What type of event are you attending? (formal/casual): ")

if temperature < 59: 
    if event_type == "formal":
        print("Warm formal suit")
    else:
        print("Cozy sweater and jeans")
elif temperature >= 59: 
    if event_type == "formal":
        print("Light formal suit")
    else:
        print("Tshirt and shorts!")