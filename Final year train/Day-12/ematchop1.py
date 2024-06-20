#given two lists from l1 if it is even add odd elements from l2 and append it to final list
#  o/p:  [13, 11, 9, 15, 9, 7, 5, 11, 11, 9, 7, 13],[48,32,40]

def matcheo(fl,i):
    def add(j,s):
        if j<len(l2):
            if l2[j]%2!=0:
                s+=(l1[i]+l2[j])
                add(j+1,s)
            else:
                add(j+1,s)
        else:
            fl.append(s)
    if i<len(l1):
        if l1[i]%2==0:
            add(0,0)
            matcheo(fl,i+1)
        else:
            matcheo(fl,i+1)
    return fl

l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
print(matcheo([],0))