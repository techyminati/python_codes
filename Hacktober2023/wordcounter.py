from collections import Counter

text = "This is a sample text. This text contains some words. Sample text is used for counting words."

words = text.split()
word_counts = Counter(words)

for word, count in word_counts.items():
    print(f"'{word}': {count} times")
