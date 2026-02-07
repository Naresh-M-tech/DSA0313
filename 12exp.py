grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["dog"]],
    "V": [["saw"]]
}

def earley_parse(words):
    chart = [set() for _ in range(len(words) + 1)]
    chart[0].add(("S", tuple(grammar["S"][0]), 0, 0))

    for i in range(len(words) + 1):
        for state in list(chart[i]):
            lhs, rhs, dot, start = state
            if dot < len(rhs):
                sym = rhs[dot]
                if sym in grammar:
                    for prod in grammar[sym]:
                        chart[i].add((sym, tuple(prod), 0, i))
                elif i < len(words) and words[i] == sym:
                    chart[i + 1].add((lhs, rhs, dot + 1, start))
            else:
                for st in chart[start]:
                    if st[2] < len(st[1]) and st[1][st[2]] == lhs:
                        chart[i].add((st[0], st[1], st[2] + 1, st[3]))

    return any(state[0] == "S" and state[2] == len(state[1]) for state in chart[len(words)])

sentence = ["the", "dog", "saw", "the", "dog"]
print("Sentence Accepted:", earley_parse(sentence))
