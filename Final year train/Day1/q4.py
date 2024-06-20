#i/p=placements  o/p=plAcEmEnts
'''st="placements"
for i in st:
    if i in "aeiou":
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")'''

# i/p=5 3.8 7 5.6 4 2 3    o/p=(adding even/odd/decimal integers separately)6 15 9.4

val=list(map(float,input().split(" ")))
es,os,ds=0,0,0
for i in val:
    if i.is_integer():
        if i%2==0:
            es+=i
        else:
            os+=i
    else:
        ds+=i
print("Even sum:",int(es))
print("Odd sum:",int(os))
print("Decimal sum:",ds)
