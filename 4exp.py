def pluralize(noun):
    state = "START"

    if noun.endswith(("s", "x", "z", "ch", "sh")):
        state = "ADD_ES"
    elif noun.endswith("y") and noun[-2] not in "aeiou":
        state = "Y_TO_IES"
    else:
        state = "ADD_S"

    if state == "ADD_ES":
        return noun + "es"
    elif state == "Y_TO_IES":
        return noun[:-1] + "ies"
    else:
        return noun + "s"


words = ["cat", "bus", "baby", "box"]

for w in words:
    print(w, "→", pluralize(w))
