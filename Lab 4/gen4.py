def squares(a, b):
    
    for i in range(a, b+1):
        yield i**2

for i in squares(int(input()), int(input())):
    print(i, end = " ")