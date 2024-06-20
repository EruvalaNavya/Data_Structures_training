def bfs(start,l):
    queue=[]
    var=0
    queue.append(start)
    while queue:
        var=queue.pop(0)
        l.append(var)
        for val in graph[var]:
            if val not in l and val not in queue:
                queue.append(val)
    print(l)

graph={5:[7,3],
       7:[5,4,3],
       4:[7,8,2],
       8:[3,4,2,12],
       3:[5,7,8],
       2:[4,8,9],
       12:[8,1],
       9:[2],
       1:[12]
}
'''graph={1:[2,3,4,5],
       2:[1,7],
       3:[1],
       4:[1,6],
       5:[1,9],
       6:[4,8],
       7:[2,8],
       8:[6,7],
       9:[5]
}'''
bfs(5,[])