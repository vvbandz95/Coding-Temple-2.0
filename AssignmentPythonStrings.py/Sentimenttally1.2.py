#1.2 Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.

def count_sentiments(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0

    for review in reviews:
        words = review.lower().split()
        
        for word in words:
            if word in positive_words:
                positive_count += 1
            if word in negative_words:
                negative_count += 1

    return positive_count, negative_count

reviews = ["This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

positive_count, negative_count = count_sentiments(reviews, positive_words, negative_words)

print("Total positive words:", positive_count)
print("Total negative words:", negative_count)
