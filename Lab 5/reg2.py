import re

pattern2 = re.compile(r"ab{2,3}")
matches = pattern2.findall("ab abb abbb abbbb")
print(matches)