# 6 Reviews 

product = "Kindle Paperwhite"
ave_rating = 4.7 #using a float to represent star rating
numberof_rev = 25000 #using integer for # of reviews 

if product == "Kindle Paperwhite":
    if ave_rating >= 4.5 and numberof_rev > 10000:
        print("Highly recommended product")
    elif ave_rating >= 4.0 and numberof_rev > 5000: 
        print("A well received product")
    elif ave_rating < 4.0: 
        print("Product has mixed reviews")
    else: 
        print("The pdrocut has high rating but lacks reviews")

elif product == "Amazon Echo":
    if ave_rating >= 4.5 and numberof_rev > 15000:
        print("top rated speaker lots of reviews")
    elif ave_rating >= 4.0 and numberof_rev > 7000: 
        print("ppopular smart device")
    elif ave_rating < 4.0: 
        print("Speaker has varied reviews")
    else: 
        print("The smart speaker has varied reviews")

elif product == "Amazon Fire Stick":
    if ave_rating >= 4.5 and numberof_rev > 20000:
        print("Must have for streaming enthusiasts")
    elif ave_rating >= 4.0 and numberof_rev > 8000: 
        print("A favorite among many")
    elif ave_rating < 4.0: 
        print("Firestick has mixed feedback")
    else: 
        print("Firestick seems promising")

else: 
    print("Please check product's detailed reviews and ratings on Amazon")