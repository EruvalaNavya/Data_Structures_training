'''
i/p: 3x4
    a - - -
    - - - -
    - - - b
o/: number of paths from a to b
'''
'''def paths(vis,i,j):
    if i==n-1 and j==m-1:
        return 1
    if i<0 or i>=n or j<0 or j>=m or vis[i][j]==1:
        return 0 
    vis[i][j]=1
    top=paths(vis,i-1,j)
    bottom=paths(vis,i+1,j)
    left=paths(vis,i,j-1)
    right=paths(vis,i,j+1)
    vis[i][j]=0
    return top+bottom+left+right
'''
def fun(i,j,c):
    if i<0 or i>=n or j<0 or j>=m:
        return c
    if i==n-1 and j==m-1:
        #print(vis)   -->to get the paths
        c=c+1
        return c
    vis.append((i,j))
    if (i-1,j) not in vis:
        c=fun(i-1,j,c)
    if (i+1,j) not in vis:
        c=fun(i+1,j,c)
    if (i,j-1) not in vis:
        c=fun(i,j-1,c)
    if (i,j+1) not in vis:
        c=fun(i,j+1,c)
    vis.pop()
    return c

n=3
m=4
vis=[]
'''for i in range(n):
    l=[0]*m
    vis.append(l)
print(paths(vis,0,0))'''
print(fun(0,0,0))