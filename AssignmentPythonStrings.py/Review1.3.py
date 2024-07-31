# 1.3 

def create_summary(review, max_length=30):
    if len(review) <= max_length:
        return review 

    cutoff = review[:max_length].rfind(' ')
    
    if cutoff == -1:
        cutoff = max_length
    
    summary = review[:cutoff].strip() + "…"
    return summary

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

for review in reviews:
    summary = create_summary(review)
    print(summary)
