def unique(list):
    uniqueList = []
    for i in list:
        if i not in  uniqueList:
            uniqueList.append(i)
    return uniqueList

list=[11, 1, 3, 2, 1, 3, 4]
print(unique(list))