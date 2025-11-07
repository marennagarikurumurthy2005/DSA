nums=[1,5,6,4,3,6,8,7,9,5,5,5,5,5,5,5,5,5,12,5,5,5,6,5,]

dici_max=0
dict={}
for i in nums:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

n=len(nums)//2
ans=-1

for i in dict:
    val=dict[i]
    if val>n:
        ans=i
print(ans)


# Optimal solution

numbers=[1,5,6,4,3,6,8,7,9,5,5,5,5,5,5,5,5,5,12,5,5,5,6,5]

same=0
count=0
for i in numbers:
    if count==0:
        same=i
    if i==same:
        count+=1
    else:
        count-=1
print(same)

# O(n^2)
dis=len(numbers)//2
new=sorted(numbers)
data=new[dis]
print(data)











    

    

