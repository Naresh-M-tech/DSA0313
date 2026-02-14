import re

expression = "Loves(John, Mary)"

pattern = r'(\w+)\((\w+),\s*(\w+)\)'
match = re.match(pattern, expression)

if match:
    predicate, arg1, arg2 = match.groups()
    print("Predicate:", predicate)
    print("Argument 1:", arg1)
    print("Argument 2:", arg2)
