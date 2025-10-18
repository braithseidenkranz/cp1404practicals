"""Estimate: 25min, Actual: 15min """

sentence = input("Enter a string: ").lower()

word_to_count = {}

words = sentence.split()

for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

max_word_length = max(len(word) for word in word_to_count)

for word in sorted(word_to_count):
    print(f"{word:{max_word_length}} : {word_to_count[word]}")