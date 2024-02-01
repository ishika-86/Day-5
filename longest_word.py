# Write a function giving the longest word in a given text.
text = input()
longest_word = max(text.split(), key = len)
print(longest_word)