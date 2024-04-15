""" 

You have been given an ilist of size M that contains 1 and 2. Write a function to arrange them in order.
function name=arrange() 
#You are not allowed to use sort function in this program

Sample Input 1:
1
7
1 2 2 2 1 2 2

Sample Output 1:

1 1 2 2 2 2 2


Sample Input 2:
2
8
2 1 2 2 1 2 1 2
5
1 2 1 2 1

Sample Output 2:
1 1 1 2 2 2 2 2

1 1 1 2 2 

"""
def arrange(n):
    a=[]
    for i in n:
        if i != '':
            if i =='1':
                a.append(i)
    for i in n:
        if i =='2':
            a.append(i)
    return a

x=int(input())
y=[]

for i in range(x):
    z=int(input())
    v=input()
    y.append(arrange(list(v)))

e=""
for ele in y:
   for i in ele:
       e=e+i+" "
   print(e[:-1])
   e=""
