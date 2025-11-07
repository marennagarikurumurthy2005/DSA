arr=[10,5,3,7,2]
n=len(arr)
# Decending
for i in range(n-1):
    is_swapped=False
    for j in range(0,n-i-1):
        if arr[j]<arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            is_swapped=True
        
            
    if is_swapped==False:
        break
print(arr)

# accesnding

for i in range(n-1):
    is_swapped=False
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            is_swapped=True
        
            
    if is_swapped==False:
        break
print(arr)

# using in built
# 1
arr.sort()
# 2
sorted(arr)

        