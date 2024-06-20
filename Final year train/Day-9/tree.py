class Node:
    def __init__(self,val):
        self.left=None
        self.data=val
        self.right=None
class tree:
    def createNode(self,x):
        return Node(x)
    def insert(self,node,x):
        if node==None:
            return self.createNode(x)
        if x < node.data:
            node.left=self.insert(node.left,x)
        else:
            node.right=self.insert(node.right,x)
        return node
    def traverse_inorder(self,root):
        if root!=None:
            self.traverse_inorder(root.left)
            print(root.data,end=" ")
            self.traverse_inorder(root.right)
    def traverse_preorder(self,root):
        if root!=None:
            print(root.data,end=" ")
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)
    def traverse_postorder(self,root):
        if root!=None:
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            print(root.data,end=" ")
    def allsum(self,root):
        if root==None:
            return 0    
        return root.data+(self.allsum(root.left))+(self.allsum(root.right))
    def evensum(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.evensum(root.left)+self.evensum(root.right) 
        else:
            return self.evensum(root.left)+self.evensum(root.right)
    def oddsum(self,root):
        if root==None:
            return 0
        if root.data%2!=0:
            return root.data+self.oddsum(root.left)+self.oddsum(root.right) 
        else:
            return self.oddsum(root.left)+self.oddsum(root.right)
    def eodiff(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return (self.eodiff(root.left)+self.eodiff(root.right))-root.data
        else:
            return root.data+self.eodiff(root.left)+self.eodiff(root.right) 
    def height(self,root):
        if root==None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    def bal(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1
    def leafnodes(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.leafnodes(root.left)+self.leafnodes(root.right)
    def leafnodesum(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.data
        return self.leafnodesum(root.left)+self.leafnodesum(root.right)
    def searchnode(self,root,x):
        if root==None:
            return
        if root.data==x:
            return 1
        if x<root.data:
            return self.searchnode(root.left,x)
        else:
            return self.searchnode(root.right,x)
    def depth(self,root,x,c):
        if root==None:
            return -1
        if root.data==x:
            return c
        if x<root.data:
            return self.depth(root.left,x,c+1)
        else:
            return self.depth(root.right,x,c+1)
    def leftview(self,root,c,l):
        if root==None:
            return
        if c not in l:
            l.append(c)
            print(root.data,end=" ")
        self.leftview(root.left,c+1,l)
        self.leftview(root.right,c+1,l)
    def rightview(self,root,c,l):
        if root==None:
            return
        if c not in l:
            l.append(c)
            print(root.data,end=" ")
        self.rightview(root.right,c+1,l)
        self.rightview(root.left,c+1,l)
    def topview(self,root,c,d,q):
        if root==None:
            return
        q.append([root,c])
        while len(q)!=0:
            r=q.pop(0)
            if r[1] not in d:
                d[r[1]]=r[0].data
            if r[0].left is not None:
                q.append([r[0].left,r[1]-1])
            if r[0].right is not None:
                q.append([r[0].right,r[1]+1])
        return d.values()
    def bottomview(self,root,c,d,q):
        if root==None:
            return
        q.append([root,c])
        while len(q)!=0:
            r=q.pop(0)
            d[r[1]]=r[0].data
            if r[0].left is not None:
                q.append([r[0].left,r[1]-1])
            if r[0].right is not None:
                q.append([r[0].right,r[1]+1])
        return d.values()

o=tree()
root=o.createNode(10)
#print(root.data)
o.insert(root,5)
o.insert(root,15)
o.insert(root,2)
o.insert(root,7)
o.insert(root,11)
o.insert(root,8)
o.insert(root,9)
'''print("Inorder traversal: ")
o.traverse_inorder(root)
print()
print("Pre-order traversal: ")
o.traverse_preorder(root)
print()
print("Post-order traversal: ")
o.traverse_postorder(root)
print()
print("All elements in tree sum:",o.allsum(root))
print("All even elements sum in tree:", o.evensum(root))
print("All odd elements sum in tree:",o.oddsum(root))
print(abs(o.eodiff(root)))
print("height of tree:")
print(o.height(root))
#-->whether Tree is balanced or not
if(o.bal(root)):
    print("Balanced tree")
else:
    print("Unbalanced tree")
print("Number of leaf node: ",o.leafnodes(root))
print("Leafnodes sum is: ",o.leafnodesum(root))
if (o.searchnode(root,10)):
    print("Found")
else:
    print("Not found")
print("Depth of element:",o.depth(root,20,0))'''
'''root=o.createNode(10)
o.insert(root,5)
o.insert(root,15)
o.insert(root,7)
o.insert(root,2)
o.insert(root,11)
o.insert(root,20)
o.insert(root,21)
o.insert(root,3)
o.insert(root,22)'''
'''print("Left view:")
o.leftview(root,0,[])
print()
print("Right view:")
o.rightview(root,0,[])
print()

print("Top view:")
dict=o.topview(root,0,{},[])
print(sorted(dict))
print("Bottom view:")
dict=o.bottomview(root,0,{},[])
print(sorted(dict))'''

