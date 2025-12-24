# 912. Sort an Array
# Medium
# Topics
# premium lock icon
# Companies
# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessarily unique.
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104

 
# brute force approach

# nums = [5,1,1,2,0,0]
# n=len(nums)

# for i in range(len(nums)):
    
#     for j in range(len(nums)):
        
#         if nums[i]<nums[j]:
#             nums[j],nums[i]=nums[i],nums[j]
#             # temp=nums[i]
#             # nums[i]=nums[j]
#             # nums[j]=temp
            
# print(nums)

# Bubble sort
# compare only neighbour elements
# for i in range(n):
#     is_sorted=True
#     for j in range(n-i-1):
#         if nums[j]>nums[j+1]:
#             temp=nums[j]
#             nums[j]=nums[j+1]
#             nums[j+1]=temp
#             is_sorted=False
#     if is_sorted==True:
#         break
            


# print(nums)


# using insertion sort
# nums = [5,1,1,2,0,0]
# n=len(nums)
# for i in range(1,n):
#     key=nums[i]
#     j=i-1
#     while j>=0 and nums[j]>key:
#         nums[j+1]=nums[j]
#         j-=1
#     nums[j+1]=key

# print(nums)
        

            
# for i in range(1,n):
#     key=nums[i]
#     j=i-1
#     while j>=0 and nums[j]>key:
#         nums[j+1]=nums[j]
#         j-=1
#     nums[j+1]=key
# print(nums)
    

#  using Selection sort 

# nums = [5,1,4,9,8,3,0,2]
# n=len(nums)
# for i in range(n):
#     mn=nums[i]
#     idx=i
#     for j in range(i+1,n):
#         if nums[j]<mn:
#             mn=nums[j]
#             idx=j
#     nums[i],nums[idx]=nums[idx],nums[i]
# print(nums)


# Merge Sort 

nums = [5,1,4,9,8,3,0,2]
n=len(nums)

def merge_sort(nums,l,r):
    if l<r:
        mid=(l+r)//2
        merge_sort()








# def merge(left,right):
#     result=[]
#     i=j=0
    


# def merge_sort(nums):
#     if len(nums)<=1:
#         return nums
#     mid=n//2
#     left=merge_sort(nums[:mid])
#     right=merge_sort(nums[mid:])
#     return merge(left,right)




    



        


            


