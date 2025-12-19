
# brute force

# nums=[2,4,8,6,8]
# n=len(nums)
# maxi=0
# for i in range(n-2):
#     for j in range(i,i+3):
#         sub=[]
#         for k in range(i,j+1):
#             sub.append(nums[k])   
#         if len(sub)>=3:
#             val=sum(sub)
#             maxi=max(maxi,val)
# print(maxi)         



# sliding window O(n)
nums=[2,4,8,6,8]
l=0
sublen=3
n=len(nums)
temp=0
maxi=0
for r in range(n):
    temp+=nums[r]
    if r-l==sublen:
        temp-=nums[l]
        l+=1
    if r-l+1==sublen:
        maxi=max(maxi,temp)
print(maxi)




