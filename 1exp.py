import re

text = "Python is easy. Python3 is powerful."

# match() – checks only at the beginning
pattern_match = re.match("Python", text)
if pattern_match:
    print("Match found:", pattern_match.group())
else:
    print("No match at beginning")

# search() – searches anywhere in the string
pattern_search = re.search("Python3", text)
if pattern_search:
    print("Search found:", pattern_search.group())
else:
    print("Pattern not found")
