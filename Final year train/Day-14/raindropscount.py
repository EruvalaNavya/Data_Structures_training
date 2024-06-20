#there are n buildings with some heights and find the max rain water stored in between them
# i/p=[2,5,2,3,6,7,1,0,5,7]  o/p=20  ;  i/p=[4,3,4,5,6,1,0,6,7]   o/p=12
l=[2,7,2,3,4]
'''s=0
i1,j1=0,0
mx1,mx2=0,0
for i in range(len(l)):
    if l[i]>=mx1:
        mx1=l[i]
        i1=i
        if mx1>=mx2:
            mx2=mx1
            t=j1
            j1=i
            print(t,mx2,j1,mx1)
            for k in range(t+1,j1):
                s=s+(l[t]-l[k])
else:
    s+=(mx2-l[i])
print("Total number of raindrops:",s)'''

#method 2
'''
h=[2,4,2,3,4,4,1,0,5,4]
n=len(h)
minb=[]
maxb=[]
m=0
s=0
for i in range(n):
    if(h[i]>m):
        m=h[i]
    minb.append(m)
x=0
print
for i in range(n-1,-1,-1):
    if x<h[i]:
        x=h[i]
    maxb.insert(0,x)
print(minb)
print(maxb)
for i in range(n):
    s=s+(min(minb[i],maxb[i])-h[i])
print(s)
'''
