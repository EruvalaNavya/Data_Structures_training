#i/p=  tu5g2k1h8,g5g8gd6h3   o/p=forming largest even number-->865312

s1="tu5g2k1h8"
s2="g5g8gd6h3"
l=[]
for i in s1:
    if i.isdigit() and int(i) not in l:
        l.append(int(i))
for i in s2:
    if i.isdigit() and int(i) not in l:
        l.append(int(i))
l.sort(reverse=True)
print(l)
l1=""
val=0
c=0
if l[-1]%2!=0:
    for i in range(len(l)-2,-1,-1):
        if l[i]%2==0:
            val=l[i]
            l.remove(val)
            l.append(val)
            break
        else:
            c=c+1
    if c==len(l)-1:
        print("-1")
    else:
        for i in l:
            l1+=str(i)
        print(l1)
   


