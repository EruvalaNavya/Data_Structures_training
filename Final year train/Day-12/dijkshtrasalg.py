def mincostpath(start):
    d[start]=0
    queue=[]
    vis=[]
    queue.append(start)
    while queue:
        x1=9999
        for i in queue:
            if d[i]<x1:
                x1=d[i]
                x=i
        for val in graph[x]:
            if val[0] not in vis:
                queue.append(val[0])
                if d[val[0]]>val[1]+d[x]:
                    d[val[0]]=val[1]+d[x]
        vis.append(x)
        queue.remove(x)
graph={5:[(3,4),(7,2)],
       7:[(5,2),(4,1),(3,2)],
       4:[(7,1),(8,1),(2,3)],
       8:[(3,3),(4,1),(2,5)],
       3:[(5,4),(7,2),(8,3)],
       2:[(4,3),(8,5)]
}
d={5:99,7:99,4:99,8:99,3:99,2:99}
mincostpath(5)
print(d)