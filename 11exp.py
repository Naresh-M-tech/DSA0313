grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["chased"], ["saw"]]
}

def parse(symbol, tokens):
    if not tokens:
        return False
    if symbol not in grammar:
        return tokens[0] == symbol
    for rule in grammar[symbol]:
        temp = tokens[:]
        valid = True
        for sym in rule:
            if not temp or not parse(sym, temp):
                valid = False
                break
            temp.pop(0)
        if valid:
            return True
    return False

sentence = ["the", "cat", "chased", "the", "dog"]
print("Sentence Accepted:", parse("S", sentence))
