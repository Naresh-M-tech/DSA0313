import random

text = "natural language processing is fun and language processing is useful"
tokens = text.split()

bigrams = {}
for i in range(len(tokens) - 1):
    pair = tokens[i]
    next_word = tokens[i + 1]
    if pair not in bigrams:
        bigrams[pair] = []
    bigrams[pair].append(next_word)

word = random.choice(tokens)
generated_text = [word]

for i in range(10):
    if word in bigrams:
        word = random.choice(bigrams[word])
        generated_text.append(word)
    else:
        break

print("Generated Text:")
print(" ".join(generated_text))
