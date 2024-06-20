'''
o/p:
['hello:5438', 'car:214', 'book:8799', 'apple:2187']
oaxp length of hello is 5 , append 5th element in string, if not next smallest number index+1 element
'''
s="hello:5438,car:214,book:8799,apple:2187".split(",")
'''c=0
l=[]
l1=[]
for i in range(len(s)):
    for j in s[i]:
        if j!=':':
            l.append(j)
    l1.append(l)
    l=[]
#print(l1)
st=''
for i in l1:
    for j in range(len(i)):
        if i[j].isalpha():
            c=c+1
        else:   
            if str(c) in i[j:]:
                st=st+i[c-1]
                c=0
                break
    
    
print(st)'''

s1=''
for i in s:
    a=i.split(":")
    ln=len(a[0])
    if str(ln) in a[1]:
        s1=s1+a[0][-1]
    else:
        for i in range(ln-1,0,-1):
            if str(i) in a[1]:
                s1=s1+a[0][i-1]
                break
        else:
                s1=s1+'x'
print(s1)

        
