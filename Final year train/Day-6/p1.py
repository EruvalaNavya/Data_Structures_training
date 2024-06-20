#print most occurence number   o/p=[4,8,2,4,4,4,8]  o/p=4
'''l=list(map(int,input().split(",")))
c=1
win=l[0]
for i in range(1,len(l)):
    if win==l[i]:
        c=c+1
    else:
        c=c-1
        if c==0:
            win=l[i]
            c=1
print(win)'''
# i/p=7  0 5 3 6 7 2 1   o/p=missing number-->4
'''n=7
l=[0,5,3,6,7,2,1]
for i in range(n+1):
    if i not in l:
        print(i)
        break'''
'''s=sum(l)
   n=(n*(n+1))//2
   print(s-n)'''

#finding largest factor of given number  i/p=12 2(2nd largest)    o/p=6
'''n=12
k=3
c=0
for i in range(n,0,-1):
    if n%i==0:
        c=c+1
        if k==c:
            print(i)
            break'''
#co-prime numbers
'''n1=int(input())
n2=int(input())
c=0
for i in range(1,(min(n1,n2)//2)+1):
    if n1%i==0 and n2%i==0:
        print("Not co-prime")
        break
else:
    print("co-prime")'''
#unbalanced parenthesis
s="(([{}]))"
stack=[]
for i in s:
    if i=='(' or i=='[' or i=='{':
        stack.append(i)
    elif (stack[-1]=='(' and i==')') or (stack[-1]=='[' and i==']') or (stack[-1]=='{' and i=='}'):
        stack.pop()
if len(stack)==0:
    print("-1")
else:
    print(s.index(i))
#using double linked list unbalanced parenthesis

    
        

            
