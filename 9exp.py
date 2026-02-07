import re

rules = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*s$', 'NNS'),
    (r'.*ly$', 'RB'),
    (r'.*', 'NN')
]

sentence = "Dogs are barking loudly"
words = sentence.split()

print("Rule-Based POS Tagging:")
for word in words:
    for pattern, tag in rules:
        if re.match(pattern, word.lower()):
            print(word, "->", tag)
            break
