def check_agreement(sentence):
    singular_subjects = ["he", "she", "it", "dog"]
    singular_verbs = ["runs", "eats"]

    words = sentence.lower().split()
    subject = words[1]
    verb = words[2]

    if subject in singular_subjects and verb in singular_verbs:
        return "Agreement Correct"
    else:
        return "Agreement Incorrect"

sentence = "The dog runs"
print("Sentence:", sentence)
print(check_agreement(sentence))
