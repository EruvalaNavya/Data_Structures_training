#minimum number of coins to get sum using dynamic programming(Tabulation)
l=[1,3,4,5]
n=17
dp=[]
for i in range(len(l)): 
    l1=[0]*(n+1)
    dp.append(l1)
for i in range(len(l)):
    for j in range(1,n+1):
        if j<l[i]:
            dp[i][j]=dp[i-1][j]
        elif j>=l[i]:
            dp[i][j]=dp[i][j-l[i]]+1
            if  i!=0 and dp[i-1][j]<dp[i][j]:
                dp[i][j]=dp[i-1][j]
print(dp,end=" ")

#using list
def fun():
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range(1,n+1):
            if j>=i:
                if l1[j-i]!=-1:
                    if l1[j]!=-1:
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1)


l=[3,4,5]
n=7
fun()