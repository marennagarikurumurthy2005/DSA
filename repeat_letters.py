arr=['a','a','b','b','c','a']
i=0
while i<len(arr):
    count=0

    for j in range (i,len(arr)):
        if arr[i]!=arr[j]:
            break
        else:
            count+=1
    print(f"{count}{arr[i]}",end="")
    i+=count

#using dictonary 

dict={}
for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

for i in dict:
    print(i,dict[i])

        
        
    
    
    
        

