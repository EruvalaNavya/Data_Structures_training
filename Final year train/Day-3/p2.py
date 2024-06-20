#palindrome using recursion
'''def pal(n,dn):
    if n==0:
        return dn
    dn=dn*10+(n%10)
    return pal(n//10,dn)
n=int(input())
x=pal(n,0)
if x==n:
    print("Pal")
else:
    print("Not pal")'''
#i/p=15 3 2 7 8 4    o/p=6
#     m t w t f s
'''l=list(map(int,input().split()))
s=[]
s1=0
for i in range(len(l)-1):
    j=i+1
    while(j<len(l)):
        s.append(l[j]-l[i])
        j=j+1
    s1=max(s)
print(s1)'''
'''l=list(map(int,input().split()))
s,b=l[0],l[0]
p=0
for i in range(1,len(l)):
    if l[i]>b and (l[i]-b)>p:
        s=l[i]
        p=s-b
    else:
        b=l[i]
print(p)'''
#i/p=5  o/p=1-9 surrounded by *
'''n=5
k=1
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(k,end=" ")
            k=k+1
    print()'''
#i/p=4  o/p=_ _ _ _ a _ _ _ _ ,_ _ _ aba_ _ _,......._abcdcba_

n=4
k=97
x=0
for i in range(n):
    for j in range(n):
        if j<n-i-1:
            print("_",end=" ")
        else:
            print(chr(k),end=" ")
            k=k+1
    print()
            















