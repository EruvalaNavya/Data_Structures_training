l=[3,5,9,6,8,10]
mx=l[0]
c=1
#for front side sunlight
for i in range(1,len(l)-1):
    if mx<l[i+1]:
        mx=l[i+1]
    if mx>l[i]:
        c=c+1
print(c)
#for backside sunlight
c1=1
mx1=len(l)-1
for i in range(-1,-1):
    if mx>l[i-1]:
        mx=l[i-1]
    if mx<l[i]:
        c1=c1+1
print(c1)


