from random import choice

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common... it's a shame they'll never meet.",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
]

def get_random_joke():
    print(choice(jokes))

