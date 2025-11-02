# 1108. Defanging an IP Address
# Easy
# Topics
# premium lock icon
# Companies
# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

 

# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:

# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"

new_str=""
def fun(address):
    global new_str
    for i in address:
        if i==".":
            new_str+="[.]"
        else:
            new_str+=i
    return new_str
result=fun("1.1.1")
print(result)

