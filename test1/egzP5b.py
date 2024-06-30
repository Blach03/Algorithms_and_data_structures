from egzP5btesty import runtests 

def koleje ( B ):

    B.sort(key=lambda x:x[0])
    x=B[-1][0]

    B.sort(key=lambda x:x[1])
    y=B[-1][1]

    G = [[] for _ in range(max(x,y)+1)]
   
    for edge in B:

        if edge[1] not in G[edge[0]]:
            G[edge[0]].append(edge[1])
        if edge[0] not in G[edge[1]]:
            G[edge[1]].append(edge[0])

    def br(G):
        def dfsvisit(G, u, parent, time):
            nonlocal low, distance, bridges
            distance[u] = time
            low[u] = time
            visited[u] = True

            for v in G[u]:
                if not visited[v]:
                    dfsvisit(G, v, u, time + 1)
                    low[u] = min(low[u], low[v])

                    if low[v] == distance[v]:  # Wykrywanie mostu
                        bridges.append((u, v))
                elif v != parent:
                    low[u] = min(low[u], distance[v])

        n = len(G)
        low = [float('inf')] * n
        distance = [float('inf')] * n
        visited = [False] * n
        bridges = []
        time = 0

        for u in range(n):
            if not visited[u]:
                dfsvisit(G, u, None, time)

        return bridges

    bridges=br(G)
    list_of_points=[]
    for el in bridges:
        if el[0] not in list_of_points:
            list_of_points.append(el[0])
        if el[1] not in list_of_points:
            list_of_points.append(el[1])
    sum=0
    for point in list_of_points:
        if len(G[point])>1:
            sum+=1
    return sum

runtests ( koleje, all_tests=True )