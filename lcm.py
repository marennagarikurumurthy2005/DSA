num1=2
num2=3
lcm=num1*num2
for i in range(1,num1*num2+1):
    if i%num1==0 and i%num2==0:
        lcm=min(lcm,i)
        break
print(lcm)
    