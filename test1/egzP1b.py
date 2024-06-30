from egzP1btesty import runtests 
from collections import deque
def turysta( G, D, L ):
    q=deque()
    newg=[[] for _ in range(L+1)]
    if L>50: return 0
    visited=[False]*(L+1)
    visited[D]=True
    dist=[float('inf')]*(L+1)
    dist[D]=0
    paths=[]
    for edge in G:

        newg[edge[0]].append((edge[1],edge[2]))
        newg[edge[1]].append((edge[0],edge[2]))


    q.append((D,0))
    while q:
        v=q.popleft()
        if v[1]>3: continue
        for neighbour,weight in newg[v[0]]:
            if neighbour==L and v[1]!=3:
                continue
            if visited[neighbour]:
                if dist[neighbour]>dist[v[0]]+weight:
                    dist[neighbour] = dist[v[0]] + weight
            else:
                visited[neighbour]=True
                q.append((neighbour,v[1]+1))
    print(dist)
    print(D,L,newg)
    return dist[L]

runtests ( turysta )