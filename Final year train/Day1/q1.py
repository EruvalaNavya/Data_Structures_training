#to print sorted lists

l1=[2,5,7,9]
l2=[1,3,6,7,10,13]
#print(sorted(l1+l2))
'''l=l1+l2
l.sort()
print(l)'''
#using merge sort
c=[]
i,j=0,0
while(i<len(l1) and j<len(l2)):
    if l1[i] < l2[j]:
        c.append(l1[i])
        i=i+1
    else:
        c.append(l2[j])
        j=j+1
if i<len(l1):
    c.extend(l1[i:])
if j<len(l2):
    c.extend(l2[j:])
''' for java to add extra
while j<len(l2):
    c.append(l2[j])
    j=j+1
while i<len(l1):
    c.append(l1[i])
    i=i+1'''
print(c)
