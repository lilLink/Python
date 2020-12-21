import re

text = input("Input text: ")
words = re.split(r'[^a-zA-Z0-9]+', text)

print(sorted(words, key=lambda x:(str.lower(x),x)))