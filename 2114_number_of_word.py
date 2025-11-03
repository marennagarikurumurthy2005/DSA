# sentence="im kurumurthy & from nirven"
# count=1
# for i in range(len(sentence)):
#     if sentence[i]==" ":
#         count+=1
# print(count)
maxi=0
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
for i in range(len(sentences)):
    count=1
    temp=sentences[i]
    for j in range(len(temp)):
        if temp[j]==" ":
            count+=1
    maxi=max(maxi,count)
print(maxi)