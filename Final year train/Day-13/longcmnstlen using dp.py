s1="abcd"
s2="axbdc"
n=len(s1)
m=len(s2)
mat=[]
#to get the count
for i in range(n+1):
    l=[0]*(m+1)
    mat.append(l)
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]:
            mat[i][j]=mat[i-1][j-1]+1
        else:
            mat[i][j]=max(mat[i][j-1],mat[i-1][j])
print(mat[n][m])
#to get the string
res=""
while n!=0 and m!=0:
    if s1[n-1]==s2[m-1]:
        res=s1[n-1]+res
        n=n-1
        m=m-1
    else:
        if mat[n][m]==mat[n][m-1]:
            m=m-1
        elif mat[n][m]==mat[n-1][m]:
            n=n-1
print(res)