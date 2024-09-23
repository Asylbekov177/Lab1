fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ["hello" for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)