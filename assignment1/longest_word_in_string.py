words = ["apple", "banana", "cherry", "watermelon", "pear"]
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
