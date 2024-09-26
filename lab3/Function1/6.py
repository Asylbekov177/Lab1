def reverse(string):
    reverse_list=string.split(" ")
    reverse_list.reverse()
    for i in reverse_list:
        print (i, end=" ")
    

string = str(input())
reverse(string)
