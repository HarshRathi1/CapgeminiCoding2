'''Capgemini in its online written test have a coding question, wherein the students are given a string with multiple characters that are repeated consecutively. You’re supposed to reduce the size of this string using mathematical logic given as in the example below :
Input :
aabbbbeeeeffggg
Output:
a2b4e4f2g3'''
s="aabbbccddddeff"
r=''
for i in s:
    if i not in r:
        if s.count(i)>1:
            r+=i+str(s.count(i))
        else:
            r+=i
print(r)

