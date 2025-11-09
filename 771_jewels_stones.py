# 771. Jewels and Stones
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0

# def func(jewels,stones):
#     count=0
#     # for i in stones:
#     #     if i in jewels:
#     #         count+=1
#     #     else:
#     #         pass
#     for i in stones:
#         for j in jewels:
#             if i==j:
#                 count+=1
#                 break
#             else:
#                 pass
#     return count 

# result=func("aAbaBa","AabbCCC")
# print(result)




jewels = "aA"
stones = "aAAbbb"
dict={}
count=0
for i in stones:
    
    if i in jewels:
        
        if i in dict:
            
            
            dict[i]+=1
            
        else:
            
            dict[i]=1
        count+=1




# for i in dict:
#     count+=dict[i]

print(count)


