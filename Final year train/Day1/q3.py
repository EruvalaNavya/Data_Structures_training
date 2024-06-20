#input:3 5 4 3 6 7 1 2 4 3 3 7 6 8 8
#op:3-4,5-1,4-2,6-2,7-2,1-1,2-1,8-2
'''a=[3,5,4,3,6,7,1,2,4,3,3,7,6,8,8]
b=[]
for i in a:
    if (i not in b):
        b.append(i)
for i in b:
    print(i,"-",a.count(i))'''
#i/p=f46feLK9y56u#@&56hIjbn6KJhA   o/p=lv- 2,uv- 2,lc- 8,uc- 4,d- 8,s-3
st="f46feLK9y56u#@&56hIjbn6KJhA"
lc=[]
uc=[]
dc=0
sc=0
lv,uv,lcn,ucn=0,0,0,0
for i in st:
    if i.islower():
        lc.append(i)
    elif i.isupper():
        uc.append(i)
    elif i.isdigit():
        dc=dc+1
    elif not i.isalnum():
        sc=sc+1
for i in lc:
    vowels="aeiou"
    if i in vowels:
        lv=lv+1
    else:
        lcn=lcn+1
for i in uc:
    vowels="AEIOU"
    if i in vowels:
        uv=uv+1
    else:
        ucn=ucn+1

print("Lower vowels:",lv)
print("Lower consonants:",lcn)
print("Upper vowels:",uv)
print("Upper consonants:",ucn)
print("Digit count:",dc)
print("Special symbols:",sc)

#i/p=placements  o/p=plAcEmEnts
st="placements"
for i in st:
    if i in "aeiou":
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")


