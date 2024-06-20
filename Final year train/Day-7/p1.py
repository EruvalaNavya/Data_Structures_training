#printing 3 elements in list
'''def comb(a,k):
    def fun(l1,start):
        if len(l1)==k:
            print(l1)
            return
        for i in range(start,len(a)):
            fun(l1+[a[i]],i+1)
        return
    fun([],0)
l=list(map(int,input().split(",")))
(OR)
def comb(l,n,l1,start):
    if len(l1)==n:
        print(l1)
        return
    for i in range(start,len(l)):
        comb(l,n,l1+[l[i]],i+1)    
        
l=[3,5,1,6,7]
n=3
comb(l,n,[],0)
(OR)
l=[3,5,2,6,7]
n=3
#using for loops
 for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            l1.append([l[i],l[j],l[k]])
print(l1)
comb(l,n)'''

''' Q)  i/p=school,
    3 queries
    L 2  --> hoolsc
    R 3 -->  oolsch
    L 1  --> chools
    
    o/p=yes   -->hoc is anagram  (sch cho hoo ool)'''
'''s=input()
n=int(input())
str=[]
for i in range(n):
    b=input()
    if b[0]=='L':
        str.append(s[int(b[2])])
    else:
        str.append(s[-int(b[2])])
str.sort()
arr=[]
for i in range(len(s)-n+1):
    t=list(s[i:n+i])
    t.sort()
    arr.append(t)
#print(arr)
if str in arr:
    print("yes")
else:
    print("no")'''

#checking number is prime or not i/p=12 o/p=yes-->(1 11,2 10,....if any one pair is prime)
'''def isprime(x):
    if x==1 or x==2:
        return 1
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0
    return 1
a=int(input())
for i in range(1,(a//2)+1):
    if isprime(i) and isprime(a-i):
        print("yes")
        break
else:
    print("no")'''

# Q)  i/p=polikujmyjmnhytgbvfredcxswqaz abbcdd   o/p=bbddca
'''s="polikujmyjmnhytgbvfredcxswqaz"
ms="abbcdd" 
for i in s:
    if i in ms:
        print(i)'''
'''n=int(input())
while n:
    a=input()
    b=input()
    s=''
    for i in a:
        if i in b:
            s+=(i*b.count(i))
    print(s)
    n=n-1'''

# i/p=[13,9,4,10,5,7]   o/p=30 -->print greatest sum with alternate values
def sm(l1):
    if len(l1)==0:
        return 0
    if len(l1)==1:
        return l1[0]
    if len(l1)==2:
        return max(l1)
    left=l1[0]+sm(l1[2:])
    right=l1[1]+sm(l1[3:])
    return max(left,right)
l=[13,9,4,10,5,7]
print(sm(l))
    