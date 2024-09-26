def filter(list):
    result = []
    for i in list:
        count=0
        for j in range(1, i+1):
            if(i%j==0):
                count += 1

        if(count==2):
            result.append(i)

    return result
                
a=[1,2,4,7,8]

print(filter(a))
