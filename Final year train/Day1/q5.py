# i/p= 3000-400 o/p=count numbers divisible by 7
'''a=int(input())
b=int(input())
c=0
for i in range(a,b):
    if i%7==0:
        c+=1'''
#print(b//7 - a//7)

# i/p=14  o/p=if it is prime print otherwise print next prime number

'''def primen(num):  --->using recursion
    c=0
    for i in range(2,num//2):
        if num%i==0:
            c=c+1
    if c==0:
        print(num)
    else:
        primen(num+1)
num=int(input())
primen(num)'''
'''n=int(input())
while(1):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
            break
    if c==0:
        print(n)
        break
    else:
        n=n+1'''

#  i/p=7854   o/p=count of prime digits in number

'''num=7854
rem,c,cn=0,0,0
while num>0:
    rem=num%10
    for i in range(2,(rem//2)):
        if num%i==0:
            c+=1
            break
    if c==0:
        cn+=1
    num=num//10      
print(cn)'''
'''c=0
while(num):
    if (n%10 in [2,3,5,7]):
        c+=1
    n=n//10
print(c)'''

#string validation     i/p=asd123!@#  o/p=1    or i/p=ab  o/p=6
pas=input()
n=len(pas)
l,u,d,s=0,0,0,0
for i in pas:
    if i.isdigit():
        d=1
    elif i.islower():
        l=1
    elif i.isupper():
        u=1
    else:
        s=1
m=4-(d+l+u+s)
if (n+m)<8:
    print(8-n)
else:
    print(m)
