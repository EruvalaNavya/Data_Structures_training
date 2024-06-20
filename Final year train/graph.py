def buildgraph(edges):
    graph={}
    for edge in edges:
        pointA,pointB=edge
        if pointA not in graph:
            graph[pointA]=[]
        if pointB not in graph:
            graph[pointB]=[]
        graph[pointA].append(pointB)
        graph[pointB].append(pointA)
    return graph
def dfs_itr(graph,start):
    stack=[start]
    while stack:
        curr=stack.pop()
        print(curr,end=" ")
        for val in graph[curr]:
            stack.append(val)
def dfs_rec(graph,start):
    print(start,end=" ")
    if len(graph[start])==0:
        return
    for val in graph[start]:
        dfs_rec(graph,val)
def bfs_itr(graph,start):
    queue=[start]
    while queue:
        curr=queue.pop(0)
        print(curr,end=" ")
        for val in graph[curr]:
            queue.append(val)

edges=[['i','j'],
       ['k','i'],
       ['m','k'],
       ['l','k'],
       ['o','n']
    ]
#dynamic input
'''edges=[]
n=int(input("Enter number of edges:"))
for i in range(n):
    edges.append(input().split())
print(edges)
print(buildgraph(edges))'''
#Depth First search-traversal
graph={ 10:[20,30,40,50],
        20:[],
        30:[],
        40:[],
        50:[60],
        60:[70],
        70:[]
    }
dfs_itr(graph,10)    #using iterative
dfs_rec(graph,10)    #using recusion
#Breadth First Search---graph traversal
graph={10:[20,30,40,50],
       20:[500],
       30:[100],
       40:[200],
       50:[60],
       60:[70],
       70:[],
       500:[1000],
       100:[],
       200:[],
       1000:[]
}
bfs_itr(graph,10)