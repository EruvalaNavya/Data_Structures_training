def dfs(start,l):
    l.append(start)
    for val,cost in graph[start]:
        if val not in l:
            dfs(val,l)
    return l
def allpaths(start,end,l):
    l.append(start)
    if start==end:
        print(l)
        l.pop()
        return
    for val,cost in graph[start]:
        if val not in l:
            allpaths(val,end,l)
    l.pop()
def allpathcost(start,end,l,sm):
    l.append(start)
    if start==end:
        print(l,"-->cost=",sm)
        sm=0
        l.pop()
        return
    for val,cost in graph[start]:
        if val not in l:
            allpathcost(val,end,l,sm+cost)
    l.pop()
def mincostpath(start,end,l,sm,minsm,l1):
    l.append(start)
    if start==end:
        if sm<minsm:
            minsm=sm
            l1=l.copy()
        sm=0
        l.pop()
        return minsm,l1
    for val,cost in graph[start]:
        if val not in l:
            minsm,l1=mincostpath(val,end,l,sm+cost,minsm,l1)
    l.pop()
    return minsm,l1
graph={5:[(7,2),(3,4)],
       7:[(5,2),(4,1),(3,2)],
       4:[(7,1),(8,1),(2,3)],
       8:[(3,3),(4,1),(2,5)],
       3:[(5,4),(7,2),(8,3)],
       2:[(4,3),(8,5)]
}
'''
print("Visiting all nodes:")
print(dfs(5,[]))
print("All possible paths:")
allpaths(5,2,[])
print("All paths with cost:")
allpathcost(5,2,[],0)
print("Mincost and path:")
print(mincostpath(5,2,[],0,999,[]))'''
print("All paths from 5 to all nodes:")
for i in graph.keys():
    allpaths(5,i,[])
    print(mincostpath(5,i,[],0,999,[]))