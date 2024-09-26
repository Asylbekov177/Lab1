def spy_game(nums):

    count=0

    for i in nums:
        if(count==0 and i == 0):
            count+=1
        elif(count==1 and i==0):
            count+=1
        elif(count==2 and i==7):
            count+=1


    if(count==3):
        return True
    else:
        return False


print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,5,0]))