import re

pattern5 = re.compile(r"a.+b\Z")
text = "appleb"
matches = pattern5.findall(text)
print(matches)
