list = [ input() for i in range(int(input()))]

mult = '*'.join(i for i in list)

print(eval(mult))
