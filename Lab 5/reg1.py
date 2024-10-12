import re

pattern1 = re.compile(r"ab*")
text = "ab abb abbb a abbbabb ababab"
matches = pattern1.findall(text)
print(matches)
