#making n value ,using values in list without using repeatedly
l=[2,3,5,6]
n=7
m=[]
for i in range(len(l)):
    m.append([0]*(n+1))
for i in range(len(l)):
    for j in range(n+1):
        if j==0 or j==l[i]:
            m[i][j]=1
        elif j<l[i]:
            m[i][j]=m[i-1][j]
        elif j>l[i]:
            if m[i-1][j]==1:
                m[i][j]=m[i-1][j]
            else:
                m[i][j]=m[i-1][j-l[i]]
if m[len(l)-1][n]==1:
    print("True")
else:
    print("False")
print(m)