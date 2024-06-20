#printing nearest palindrome number
'''def pal(n):
    s=0
    t=n
    while n:
        s=s*10+(n%10)
        n=n//10
    if s==t:
        return s
    else:
        return pal(t+1)
n=56472
print(pal(n))'''
#56476
s="1234"
s1=""
s2=""
if s==s[::-1]:
    print(s)
else:
    if len(s)%2==0:
        s1=s[:len(s)//2]
        s2=s1+s1[::-1]
        if s2<s:
            s1=int(s1)+1
            s1=str(s1)
            s2=s1+s1[::-1]
            print(s2)
    else:
        s1=s[:len(s)//2+1]
        #if s1[-1]>s1[-2]:
        s2=s1+s1[-2::-1]
            #print(s2)
            #print(s1)
        if s2<s:
            s1=int(s1)+1
            s1=str(s1)
            s2=s1+s1[-2::-1]
            print(s2)

