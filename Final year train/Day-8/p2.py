#number of unburnt trees in matrix
def fun(l,i,j,n):
    if l[i][j]==0:
        return
    if l[i][j]==1:
        l[i][j]=0
    if j>0:
        fun(l,i,j-1,n)
    if j<n-1:
        fun(l,i,j+1,n)
    if i>0:
        fun(l,i-1,j,n)
    if i<n-1:
        fun(l,i+1,j,n)
l=[]
n=int(input("Enter matrix size:"))
for i in range(n):
    l.append(list(map(int,input().split())))
'''for i in range(n):
    for j in range(n):
        fun(l,0,0,n)'''
r=int(input())
c=int(input())

fun(l,r,c,n)
c1=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            c1+=1
print(c1)
