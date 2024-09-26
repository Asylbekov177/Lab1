def palindron(string):
    if(string==string[::-1]):
        return True
    else:
        return False


string=str(input())
print(palindron(string))