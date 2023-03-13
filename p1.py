import re

def count_slurs(tweet, slur_set):
    count = 0
    words = re.findall(r'\w+', tweet.lower())
    for word in words:
        if word in slur_set:
            count += 1
    return count

def rate_tweet(tweet, slur_set):
    count = count_slurs(tweet, slur_set)
    if count == 0:
        return "Clean"
    elif count == 1:
        return "Mild"
    elif count == 2:
        return "Moderate"
    else:
        return "Severe"

def main():
    # Assuming  the file contains one tweet per line
    with open('tweets.txt', 'r') as f:
        tweets = f.readlines()

    slur_set = {"racial slur word 1", "racial slur word 2", ...} # Load the set of racial slur words

    results = []
    for tweet in tweets:
        rating = rate_tweet(tweet, slur_set)
        results.append((tweet.strip(), rating))

    # output file
    with open('results.txt', 'w') as f:
        for tweet, rating in results:
            f.write(f"{tweet} - {rating}\n")

if __name__ == '__main__':
    main()
