#within given list ,print greatest prime numbers sum
def prime(x):
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0
    return 1 
def largeprime(x,y,pr):
    for i in range(x+1,y):
        if prime(i):
            if i>pr:
                pr=i
    return pr
l=[14,16,20,22]
val,s=0,0
for i in range(len(l)-1):
    val+=largeprime(l[i],l[i+1],0)
print(val)

    