# i/p=khoor 3   o/p=hello-->3 steps back
'''s="bvec"
n=30
st=""
n=n%26
for i in s:
    if (ord(i)-n)<97 or (ord(i)-n)>122:
        st=st+chr(ord(i)+26-n)
    else:
        st=st+chr(ord(i)-n)
print(st)'''

# i/p=xyzabcdefklmnopqefgh  o/p=7-->longest common substring
'''st="xyzabcdefklmnopqefgh"
c=1
c1=0
for i in range(len(st)-1):
    if (ord(st[i+1])-ord(st[i])==1):
        c=c+1
    else:
        if c>c1:
            c1=c
        c=1
print(max(c,c1))'''

#printing correct string or not-->  i/p=3 xyz pqr abc yraxpazr   o/p=yes
'''n=int(input())
st=[]
for i in range(n):
    st.append(list(input()))
s=input()
c=0
for i in range(len(s)):
    if s[i] not in st[i%n]:
        c=1
        break
    else:
        st[i%n].remove(s[i])
if c==0:
    print("yes")
    print(st)
else:
    print("no")
    print(st)'''
        
     
    
        
    
        
        
