import re

def spaces(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += ", " + word
        else:
            res += word
    return res

text = "SplitThisStringAtUppercaseLetters"
print(spaces(text))
