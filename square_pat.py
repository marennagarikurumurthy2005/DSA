# for i in range(0,5):
#     for j in range(0,50):
#         print("*",end='')
#         if j<49:
#             print("-",end='')
#         else:
#             pass
#     print("")



# r=5
# c=10
# for i in range(0,r):
#     for j in range(0,c):
#         if i==0 or i==r-1 or j==0 or j==c-1:
#             print("*",end=' ')
#         else:
#             print("  ",end="")
#     print("")

# r=20
# c=10
# for i in range(r):
#     for j in range(r-i-1):
#         print(" ",end="")
#     for k in range(c):
#         print("*",end='')
#     print()

# r=20
# c=19
# for i in range(r):
#     for j in range(0,i):
#         print(" ",end="")
#     for k in range(c):
#         print("/",end='')
#     print()



# for i in range(r-1,-1,-1):
#     for j in range(c-i):
#         print(" ",end='')
#     temp=i*2+1
#     for k in range(temp):
#         print("*",end="")
    
    
#     print()

# for i in range(r-1):
#     for j in range(c-i):
#         print(" ",end='')
#     temp=i*2+1
#     for k in range(temp):
#         print("*",end="")
    
    
#     print()


r=10
c=9
for i in range(r):
    for j in range(c-i):
        print(' ',end="")
    temp=i*2+1
    for k in range(temp):
        if i==0 or i==r-1 or k==0 or k==temp-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()


for i in range(r-1,-1,-1):
    for j in range(c-i):
        print(' ',end="")
    temp=i*2+1
    for k in range(temp):
        if i==0 or i==r-1 or k==0 or k==temp-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()



print()
print()
r=10
c=9
for i in range(r-2):
    for j in range(c-i):
        print(' ',end="")
    temp=i*2+1
    for k in range(temp):
        if i==0 or i==r-1 or k==0 or k==temp-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()


for i in range(r-2,-1,-1):
    for j in range(c-i):
        print(' ',end="")
    temp=i*2+1
    for k in range(temp):
        if i==0 or i==r-1 or k==0 or k==temp-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()