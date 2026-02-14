def classify_dialog(sentence):
    sentence = sentence.lower()
    if sentence.endswith("?"):
        return "Question"
    elif sentence.startswith("please"):
        return "Command"
    else:
        return "Statement"

dialog = [
    "How are you?",
    "Please close the door",
    "I am fine"
]

for line in dialog:
    print(line, "->", classify_dialog(line))
