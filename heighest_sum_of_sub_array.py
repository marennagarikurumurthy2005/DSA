
# brute force

nums=[2,4,8,6,8]
n=len(nums)
maxi=0
for i in range(n-2):
    for j in range(i,i+3):
        arr=[]
        for k in range(i,j+1):
            arr.append(nums[k])   
        if len(arr)>=3:
            val=sum(arr)
            maxi=max(maxi,val)
print(maxi)         

