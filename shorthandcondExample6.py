# 6 

loves_beach = True
budget = 1500 # initial budget in dollars 
high_budget = budget >= 2000

destination = "beach resort" if loves_beach and not high_budget else "luxury mountain resort"
budget -= 500 if destination == "beach resort" else 1000 #compound assignemtn

print(destination) # outpouts: beach resort
print("Remaining budget:", budget) # outputs: remaining budget: 1000