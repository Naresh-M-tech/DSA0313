sentence = ["Time", "flies", "like", "an", "arrow"]

tags = ["NN"] * len(sentence)

for i in range(len(sentence)):
    if sentence[i].endswith("s"):
        tags[i] = "VB"
    if sentence[i].lower() == "like":
        tags[i] = "IN"

print("Transformation-Based Tagging:")
for word, tag in zip(sentence, tags):
    print(word, "->", tag)
