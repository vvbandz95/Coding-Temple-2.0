# 2.2 
attendees_str = input("Enter number of attendees: ")
attendees = int(attendees_str)

venue = "large hall" if attendees > 100 else "conference room"
print(f"Venue: {venue}")

if venue == "large hall":
    if attendees > 200:
        print("Recommendations: audio system, projector")
    elif attendees > 150:
        print("Recommendations: audio system")
elif venue == "conference room":
    if attendees > 50:
        print("Recommendations: projector")
if venue == "conference room" and attendees <= 50:
    print("No additional recommendations needed.")
