import re

pattern3 = re.compile(r"[a-z]+\_")
text = "a_def_123_ghi_456_jkl"
matches = pattern3.findall(text)
print(matches)