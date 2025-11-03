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

r=10
c=5
for i in range(r,0,-1):
    for j in range(i,0,-1):
        print(" ",end="")
    for k in range(c):
        print("-",end='')
    print()
