#2.1 correct the code 

attendees_str = input("Enter number of attendees: ")
attendees = int(attendees_str)

venue = "large hall" if attendees > 100 else "conference room"
print(venue)


