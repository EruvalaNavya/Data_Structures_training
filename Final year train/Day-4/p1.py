#singly linked list
'''class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def addfront(self,x):
        t=node(x)
        t.next=self.head
        self.head=t
    def addback(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def display(self):
        t=self.head
        while t!=None:
            print(t.data,end="->")
            t=t.next
        print()
    def evensum(self):
        t=self.head
        s=0
        while t!=None:
            if (t.data%2==0):
                s=s+t.data
            t=t.next
        print(s)
    def search(self,x):
        t=self.head
        c=1
        while t!=None:
            if t.data==x:
                c=0
            t=t.next
        if c==1:
            print("Not found")
        else:
            print("found")
    def middlenode(self):
        slow=self.head
        fast=self.head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)
    def length(self):
        fast=self.head
        c=0
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            c=c+1
        if c%2==0:
            print("Even")
        else:
            print("Odd")
l1=sll()
l1.head=node(5)
l1.addfront(6)
l1.addfront(4)
l1.addback(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.display()
l1.evensum()
l1.search(100)
l1.middlenode()
l1.length()'''

#longest common subsequence length using linked list
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def addfront(self,x):
        t=node(x)
        t.next=self.head
        self.head=t
    def addback(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def display(self):
        t=self.head
        while t!=None:
            print(t.data,end="->")
            t=t.next
        print()
    def longcom(self):
        t=self.head
        m,c=0,1
        while t.next!=None:
            if (t.next.data-t.data==1):
                c=c+1
            else:
                if c>m:
                    m=c
                c=1
            t=t.next
        if c>m:
            m=c
        print(m)
    def pairs(self):
        t=self.head
        t1=t.next
        while t.next!=None:
            t1=t.next
            while t1!=None:
                print(t.data,t1.data)
                t1=t1.next
            t=t.next
    def bubblesort(self):
        i=self.head
        p=None
        while i.next!=None:
            f=0
            j=self.head
            while j.next!=p:
                if j.data>j.next.data:
                    f=1
                    j.data,j.next.data=j.next.data,j.data
                j=j.next
            if f==0:
                break
            p=j

    def swap(self):
        prev=None
        cur=self.head
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        self.head=prev
        

            
l1=sll()
l1.head=node(3)
l1.addfront(2)
l1.addback(6)
l1.addback(8)
l1.addback(10)
l1.addback(9)
l1.display()
#l1.longcom()-->print longest common subsequence
#l1.pairs()--->printing all pairs
#l1.bubblesort()
#l1.display()
l1.swap()
l1.display()
