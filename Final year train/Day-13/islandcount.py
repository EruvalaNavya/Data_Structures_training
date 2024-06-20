'''
i/p:
5
0 1 0 0 1
1 0 0 1 1
0 0 0 0 0
1 0 0 0 0
1 0 0 0 1
o/p:
Number of islands: 5

o/p:print maximum area

'''
def islandc(l,i,j,n,c1):
    if l[i][j]==0:
        return c1
    if l[i][j]==1:
        c1=c1+1
        l[i][j]=0
    if i>0:
        c1=islandc(l,i-1,j,n,c1)
    if i<n-1:
        c1=islandc(l,i+1,j,n,c1)
    if j>0:
        c1=islandc(l,i,j-1,n,c1)
    if j<n-1:
        c1=islandc(l,i,j+1,n,c1)   
    return c1


mx=0
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
c=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            c=c+1
            c2=islandc(l,i,j,n,0)
            if mx<c2:
                mx=c2
            
print("Number of islands:",c)
print("Highest island count:",mx)