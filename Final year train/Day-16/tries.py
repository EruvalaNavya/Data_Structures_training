'''
i/p:
7
1 word
1 word
2 word
True ->o/p
3 wo
True ->o/p
3 wa
False ->o/p
2 words
False ->o/p
4 wo
o/p=['wo', 'world', 'words', 'woo']
'''
class node:
    def __init__(self):
        self.d={}
        self.flag=0
class trie:
    def __init__(self):
        self.root=node()
    def insert(self,str):
        temp=self.root
        for i in str:
            if i not in temp.d:
                temp.d[i]=node()
            temp=temp.d[i]
        temp.flag=1
    def wordsearch(self,st):
        temp=self.root
        for i in st:
            if i not in temp.d:
                return False
            temp=temp.d[i]
        if temp.flag==1:
            return True
        else:
            return False
    def prefixsearch(self,str):
        temp=self.root
        temp1=self.root
        l=[]
        for i in str:
            if i not in temp.d:
                return False
            temp=temp.d[i]
        return True
    def prefixwords(self,str):
        def word(temp,l):
            if temp.flag==1:
                l1.append(l)
            for i in temp.d:
                word(temp.d[i],l+i)  
        l1=[]
        temp=self.root
        l=""
        for i in str:
            if i not in temp.d:
                return False
            l=l+i
            temp=temp.d[i]
        word(temp,l)
        return l1    
    def prefixwordslong(self,str):
        def word(temp,l):
            if temp.flag==1:
                l1.append(l)
            for i in temp.d:
                word(temp.d[i],l+i)  
        mx,ind=0,0  
        var=0
        fs=""
        l1=[]
        for i in range(len(str)):
            temp=self.root
            l=""
            for j in str[i]:
                if j not in temp.d:
                    return False
                l=l+j
                temp=temp.d[j]
            word(temp,l)
            #print(l1) 
            for k in range(len(l1)):
                if len(l1[k])>mx:
                    mx=len(l1[k])
                    ind=k
        return l1[ind]
            

obj=trie()
'''n=int(input())
for i in range(n):
    a,s=input().split()
    if a=='1':
        obj.insert(s)
    if a=='2':
        print(obj.wordsearch(s))
    if a=='3':
        print(obj.prefixsearch(s))
    if a=='4':
        pint(obj.prefixwords(s))'''
obj.insert("world")
obj.insert("words")
obj.insert("apple")
obj.insert("woo")
obj.insert("apricot")
obj.insert("wo")
obj.prefixsearch("wo")
print(obj.prefixwords("wo"))
print(obj.prefixwordslong(["wo","ap"]))
    
