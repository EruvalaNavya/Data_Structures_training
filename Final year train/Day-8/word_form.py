'''
    i/p:
    4
    t u e s
    q w w f
    r o r f
    d j l d
    word
    o/p=yes
    '''
def fun(l,i,j,k,n,s):
    if l[i][j]!=s[k]:
        return
    if l[i][j]==s[k]:
        k=k+1
        if k>=len(s):
            print("True") 
            return
    if j>0:
        fun(l,i,j-1,k,n,s)
    if j<n-1:
        fun(l,i,j+1,k,n,s)
    if i>0:
        fun(l,i-1,j,k,n,s)
    if i<n-1:
        fun(l,i+1,j,k,n,s)
    

l=[]
n=int(input("Enter matrix size:"))
for i in range(n):
    l.append(list(map(str,input().split())))
s=input()
for i in range(n):
    for j in range(n):
        if l[i][j]==s[0]:
            fun(l,i,j,0,n,s)
