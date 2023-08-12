import re
from collections import defaultdict

paragraph = """
This is a sample paragraph. It contains some words, like sample, paragraph, and words.
Let's count the frequency of each word in this paragraph!
"""

def word_frequency_counter(paragraph):
    words = re.findall(r'\b\w+\b', paragraph.lower())

    word_frequency = defaultdict(int)
    for word in words:
        word_frequency[word] += 1

    return dict(word_frequency)


print(word_frequency_counter(paragraph), sep='\n')