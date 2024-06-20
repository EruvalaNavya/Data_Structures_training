'''
i/p=6
1 word
1 word
3 wo
3 wo
4 word
2 word
 o/p= 2 False
'''

n=6
l=[]
op=""
c=0
for i in range(n):
    a=input()
    if a[0]=='1' and a[2:] not in l:
        l.append(a[2:])
    if a[0]=='2':
        if a[2:] in l:
            op=op+" "+"True"
        else:
            op=op+" "+"False"
    if a[0]=='3':
        for i in l:
            if a[2:]==i[:len(a[2:])]:
                c=c+1
                #print(l)
    if a[0]=='4':
        for i in l:
            if a[2:] in i:
                l.remove(a[2:])
                break
#print(l)
op=op+" "+str(c)
print(op)