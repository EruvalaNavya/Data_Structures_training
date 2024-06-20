#check whether given number is prime or not until it becomes single digit value
'''def s(temp,n):
    num=0
    while(temp>0):
        num=num+(temp%10)
        temp=temp//10
    if num>9:
        s(num,n)
    else:
        if num in [2,3,5,7]:
            print(n)
        else:
            s(n+1,n+1)
n=int(input())
s(n,n)'''
#Resursion with return value
'''
def fun(x,s):
    if x==len(a):
        return s
    s=s+a[x]
    return fun(x+1,s)
a=[6,7,2]
print(fun(0,0))'''
#using recursion print sum of even numbers in A,sum of odd in B lists,  i/p=[3,8,5,4,3],[5,0,9,3,2]  o/p=(12,17)
'''def add(e,o,s1,s2):
    if e==len(a) or o==len(b):
        return s1,s2
    if a[e]%2==0:
        s1=s1+a[e]
    if b[o]%2==1:
        s2=s2+b[o]
    return add(e+1,o+1,s1,s2)
a=[3,8,5,4,3]
b=[5,0,9,3,2]
x,y=add(0,0,0,0)
print(x,y)'''
#  i/p=10  o/p=sum of even numbers
'''def fun(n,s):
    if n==0:
        return s
    if n%2==0:
        s=s+n
    return fun(n-1,s)
print(fun(10,0)) ''' 
'''def fun(x):
    if x==0:
        return 0
    return x+fun(x-2)
n=13
if n%2==0:
    print(fun(n))
else:
    print(fun(n-1))'''
#  i/p= a=[5,8,9,5,2,4,7]  o/p= print "yes" if length is even,otherwise odd

a=[5,8,9,5,2,4,7]

    
