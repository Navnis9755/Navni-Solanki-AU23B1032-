""" 

Problem: Knock Knock are you there?

Input Format:

1. Take M int input from the User 
2. Get M , seperated values from a user 
3. Enter a number 'N' you are looking for

Output Format:

1. Print index on console once Found or Print 'Better Luck Next Time' to the console


"""
M=int(input())
p=input()
n=[]
n[1:]=p
i=1
for i in n:
    if i=="," or i=="":
        n.remove(i)

search_value=input("search_value:")
for i in n:
    if i==search_value:
        print(n.index(i))
        break
else:
    print('better luck next time')
