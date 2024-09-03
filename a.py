def sum(first, second):
    return first+second

def sub(first, second):
    return first-second

def mult(first, second):
    return first*second

def div(first,second):
    return first/second

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f'Сумма: {sum(a,b)} Разность: {sub(a,b)} Умножение: {mult(a,b)} Деление: {div(a,b)}')