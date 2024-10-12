import re

pattern4 = re.compile(r"[A-Z]{1}[a-z]+")
text = "Hello world"
matches = pattern4.findall(text)
print(matches)