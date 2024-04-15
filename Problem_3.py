"""
Problem 3: Reflection or Pratibimb 

Design and Develop a User Defined function named (reflection) pass the input literal 'Welcome to EN2004' and return Output Format Mentioned Below

Input Format:

1. Take M str input from the User 
2. Get M , seperated str literals from a user (Test string to pass: 'Welcome to EN2004')

Output Format:

EN2004
to
Welcome



"""
def reflection(n):
    a=[]
    b=''
    for i in n:
        if i != ',':
            b+=i
        else:
            a.append(b)
            b=''
    if b:
        a.append(b)
    c=a[::-1]
    return c
n=input()

result = reflection(n)
for word in result:
    print(word)
