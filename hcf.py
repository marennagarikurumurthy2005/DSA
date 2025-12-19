num1=18
num2=27
hcf=0
for i in range(1,min(num1,num2)):
    if num1%i==0 and num2%i==0:
        hcf=max(hcf,i)
print(hcf)