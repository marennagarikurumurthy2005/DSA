# 205. Isomorphic Strings
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.



s = "paper"
t = "title"
dic1={}
dic2={}
is_iso=False
if len(s)==len(t):
    is_iso=True
    for i in range(len(s)):
        ch1=s[i]
        ch2=t[i]
        if ch1 not in dic1 and ch2 not in dic2:
            dic1[ch1]=ch2
            dic2[ch2]=ch1
        elif ch1 in dic1 and dic1[ch1]!=ch2:
            is_iso=False
            break
        elif ch2 in dic2 and dic2[ch2]!=ch1:
            is_iso=False
            break





    #     if s[i] in dic1:
    #         dic1[s[i]]+=i
    #     else:
    #         dic1[s[i]]=i
    # for j in range(len(t)):
    #     if t[j] in dic2:
    #         dic2[t[j]]+=j
    #     else:
    #         dic2[t[j]]=j
            
    
print(dic1)
print(dic2)
print(is_iso)

    