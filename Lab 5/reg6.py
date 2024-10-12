import re

pattern6 = re.compile(r"[ ,.]")
text = "This is a sample, text."
modified_text = re.sub(pattern6, ":", text)
print(modified_text)