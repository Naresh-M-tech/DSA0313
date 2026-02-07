def fsa_ends_with_ab(string):
    state = 0  # start state

    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0
        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0

    return state == 2


test_string = "aaab"
if fsa_ends_with_ab(test_string):
    print("String accepted")
else:
    print("String rejected")
