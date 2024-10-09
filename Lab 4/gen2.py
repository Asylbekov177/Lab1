def gen(n):
    
    for i in range (0, n+1):
        if i%2==0:
            yield i   


for i in gen(int(input())):
    print(i, end=" ")