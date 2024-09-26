def has_33(nums):
    for i in nums:
        if(i+1<len(nums) and nums[i]==3 and nums[i+1]==3):
            return True
        return False

print(has_33([3, 1, 3]))