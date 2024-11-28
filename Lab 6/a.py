str = str(input())

lower=0
upper=0
for i in range(len(str)):
    if 65 <= ord(str[i]) <= 90:
        lower+=1
    else:
        upper+=1

print(lower, upper)