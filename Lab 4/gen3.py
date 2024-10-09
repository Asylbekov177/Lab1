def gen(n):
    
    for i in range (0, n+1):
        if i%3==0 and i%4==0:
            yield i   


for i in gen(int(input())):
    print(i, end=" ")