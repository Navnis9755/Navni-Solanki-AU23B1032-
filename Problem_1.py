# Navni-Solanki-AU23B1032-
"""
Given a list of length M, you need to print and find sum of the elements of list 

Input Format :

Line 1 : An int M 
Line 2 : M int elements of list seperated by ';'

Output Format:

Addition 

Constraints :
1 <= M <= 10^6

"""
M=int(input())
n=input()
a=[]
a.append(n)
sum=0
number=''

for element in a:
    if element ==';':
        a.remove(element)
for i in n:
    if i==';':
        sum+=int(number)
        number=''
    else:
        number+=i
sum+=int(number)
print(sum)        
