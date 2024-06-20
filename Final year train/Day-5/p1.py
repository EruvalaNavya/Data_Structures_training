#Double linked list
class node:
    def __init__(self,u):
        self.data=u
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=t
    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.head.prev=t
            t.next=self.head
            self.head=new  
            
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print()
    def revdisplay(self):
        temp=self.tail
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.prev
        print()
    def search(self,x):
        temp=self.head
        temp1=self.tail
        while temp!=temp1 and temp.prev!=temp1:
            if temp.data==x or temp1.data==x:
                break
            temp=temp.next
            temp1=temp1.prev
        if temp.data==x:
            print("found")
        else:
            print("Not found")
    def length(self):
        h=self.head
        t=self.tail
        while h!=t and h.prev!=t:
            h=h.next
            t=t.prev
        if h.data!=t.data:
            print("Even length")
        else:
            print("Odd length")
    def pal(self):
        h=self.head
        t=self.tail
        while h!=t and h.prev!=t:
            if h.data==t.data:
                print("palindrome")
                return
            h=h.next
            t=t.prev
        print("Not palindrome")
    def halfswap(self):
        s=self.head
        f=self.head
        while f!=None:
            f=f.next.next
            s=s.next
        self.tail.next=self.head
        self.head.prev=self.tail
        self.tail=s.prev
        s.prev.next=None
        s.prev=None
        self.head=s
    def changinglink(self):
        t3=None
        t=self.head
        t1=self.head.next
        while t!=None:
            if t==self.head:
                t.next=t1.next
                t1.next=t
                t1.prev=t3
                t.prev=t1
                self.head=t1
                t,t1=t1,t
                t3=t1
            else:
                t.next=t1.next
                t1.next=t
                t1.prev=t3
                t.prev=t1
                t3.next=t1
                t,t1=t1,t
                t3=t1
            if t1.next!=None: 
                t1=t1.next.next
            t=t.next.next
    def parenthesis(self):
        f=self.head
        c=1
        stack=[]
        while f:
            if f.data=='(' or f.data=='[' or f.data=='{':
                stack.append(f.data)
                c=c+1
            elif (stack[-1]=='(' and f.data==')') or (stack[-1]=='[' and f.data==']') or (stack[-1]=='{' and f.data=='}'):
                stack.pop()
                c=c+1
            f=f.next
        if len(stack)==0:
            print("-1")
        else:
            print(c)
    def evnodsumdiff(self,t,es,os):
        if t==None:
            return abs(es-os)
        if (t.data)%2==0:
            es=es+t.data
        else:
            os=os+t.data
        t=t.next
        return self.evnodsumdiff(t,es,os)  
    def primecnt(self,temp,c):
        if temp==None:
            return c
        def prim(val,i):
            if (i>=(val//2)+1):
                return 1
            if val%i==0:
                return 0
            return (val,i+1)
        if prim(temp.data,2):
            c=c+1
        return self.primecnt(temp.next,c)
                
            
obj=dll()
#obj.addfront(3)
#obj.addback(4)
#obj.addback(5)
#obj.addback(6)
#obj.addback(2)
#obj.addback(1)
#obj.addback(7)
#obj.addback(8)
#obj.display()
#obj.revdisplay()
#obj.search(30)
#obj.length()
#obj.pal()
#obj.halfswap()
#obj.display()
#obj.revdisplay()
#obj.changinglink()
#obj.addfront('(')
#obj.addback('{')
#obj.addback('(')
#obj.addback(')')
#obj.addback(']')
#obj.addback(']')
#obj.display()
#obj.parenthesis()
#print(obj.evnodsumdiff(obj.head,0,0))
obj.addfront(7)
obj.addback(4)
obj.addback(5)
obj.addback(6)
obj.addback(2)
obj.addback(3)
obj.display()
print("Count of prime numbers in linked list:",obj.primecnt(obj.head,0))

