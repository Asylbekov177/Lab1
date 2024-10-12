import re

def camel_to_snake(text):
    res = ""
    pattern = re.compile(r"[A-Z][a-z]+")
    words = pattern.findall(text)
    for i, word in enumerate(words):
        if i != 0:
            res += "_" + word.lower()
        else:
            res += word.lower()
    return res

text = "SplitThisStringAtUppercaseLetters"
print(camel_to_snake(text))