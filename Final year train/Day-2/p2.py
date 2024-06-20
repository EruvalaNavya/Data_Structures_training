'''
s="MMFFMFFMFMFMFFMMFFMMF"
cm,cf=0,0
for i in s:
    if i=='M':
        cm=cm+1
    else:
        cf=cf+1
if cm==cf:
    print("0")
elif cm>cf:
    print("Male")
else:
    print("Female")'''
#removing star from string
'''st="leet**cod*e"
s=[]
for i in st:
    if i!='*':
        s.append(i)
    else:
        s.pop()
print(''.join(s))'''
#organize the sentence in sequence order
st="is2 sentence4 This1 a3".split()
s=[0]*len(st)
for i in st:
    s[int(i[-1])-1]=i[:-1]
print(' '.join(s))
    
    
    
