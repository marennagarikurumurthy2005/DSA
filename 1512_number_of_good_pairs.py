# 1512. Number of Good Pairs
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


def func(nums):
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                count+=1
            
    return count



nums =[1,1,1,1]
result=func(nums)
print(result)


#  optimal solution

dict={}
for i in nums:
    
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=0
print(dict)

def sum(num):
    if num==0:
        return num
    return num+sum(num-1)

target=0
for j in dict:
    num=dict[j]
    if num>0:
        # target+=sum(num)
        target+=(num*(num+1))/2
        target=int(target)
print(target)








