data="Kurumurthy"
n=len(data)
subs=[]
for i in range(n):
    for j in range(i,n):
        temp=""
        for k in range(i,j+1):
            temp+=(data[k])
        subs.append(temp)
print(subs)


# subarray substrings subsequence