#placing n queens

'''def solveNQueens(n):
        res=[]
        col=[]
        posdiag=[]
        negdiag=[]
        board=[["."]*n for i in range(n)]
        def queen(r):
            if r==n:
                l=["".join(i) for i in board]
                res.append(l)
                return 
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                board[r][c]="Q"
                col.append(c)
                posdiag.append(r+c)
                negdiag.append(r-c)
                queen(r+1)
                board[r][c]="."
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
        queen(0)
        return res
n=4
print(solveNQueens(n))'''
#mathod 2-->using recursion

def queen(i):
    if i==n:
        return 
    if i!=n1:
        for j in range(n):
            if check(i,j):
                mat[i][j]=1
                break
            mat[i][j]=0
    return queen(i+1)
        

def check(row,col):
    if col==m1:
        return 0
    u,v=row,col
    for i in range(u+1):   #for column checking
        if mat[i][col]==1:
            return 0
    row=u
    while(row>=0 and col>=0):   #for left diagonal checking
        if mat[row][col]==1:
            return 0
        row=row-1
        col=col-1
    while(u>=0 and v<n):   #for right diagonal checking
        if mat[u][v]==1:
            return 0
        u=u-1
        v=v+1
    return 1

n=5
n1,m1=1,3 #rook position
mat=[]
for i in range(n):
    mat.append([0]*n)
mat[0][0]=1
queen(0)
c=0
for i in range(n):
    for j in range(n):
        if mat[i][j]==1:
            c=c+1
print(mat)
print(c)
