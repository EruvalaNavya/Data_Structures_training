# o/p=[[2,3,1,4],[3,2],[3]]-->placing unique elements in list
'''l=[2,3,1,3,4,3,2]
s=[]
l1=[]
c=0
while c!=len(l):
    for i in range(len(l)):
        if l[i] not in l1 and l[i]>0:
            l1.append(l[i])
            l[i]=-1
            c+=1
    s.append(l1)
    l1=[]
print(s)'''
#OR using dictionary
'''d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
while c!=len(l):
    for i in d:
        if d[i]!=0:
            d[i]=d[i]-1
            c=c+1
            l1.append(i)
    s.append(l1)
    l1=[]
print(s)'''

# print yes if smallcase alphabets are present ,otherwise no
'''s="the 4Quick b&rown fox jumps over the lazy dog"
s=s.lower()
s1=""
for i in s:
    if i not in s1 and i!=" " and i.islower():
       s1=s1+i
if len(s1)==26:
    print("yes")
else:
    print("no")
print(s1)'''
#using dictionary
'''a=input()
d=[0]*26
for i in a:
    if i.islower():
        d[ord(i)-97]+=1
print(all(d))'''

##print length of longest substring without repeating characters
s="abcdefadbc"
s1=""
c,c1,i=0,0,0
'''while c!=len(s):
    for i in range(c,len(s)):
        if s[i] not in s1:
            s1=s1+s[i]
        else:
            if len(s1)>c1:
                c1=len(s1)
                s1=""        
    c=c+1          
print(c1)'''
'''i=0
d={}
while i<len(s):
    if s[i] not in s1:
        s1=s1+s[i]
        d[s[i]]=i
    else:
        if len(s1)>c1:
            c1=len(s1)
        s1=""
    i=d[s[i]]+1
if len(s1)>c1:
    c1=len(s1)
print(c1)'''
                
    