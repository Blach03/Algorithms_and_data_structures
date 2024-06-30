from egzP3btesty import runtests 
from queue import PriorityQueue

def lufthansa ( G ):
    from queue import PriorityQueue
    # elogv
    def dijkstra(G, s):
        n = len(G)
        parent = [None] * n
        dist = [float('inf')] * n
        dist[s] = 0
        q = PriorityQueue()
        q.put((s, 0))
        visited = [False] * n

        while not q.empty():
            v, dst = q.get()
            if visited[v]:
                continue
            visited[v] = True

            for u, weight in G[v]:
                if not visited[u]:
                    new_dist = dist[v] + weight
                    if new_dist < dist[u]:
                        dist[u] = new_dist
                        parent[u] = v
                        q.put((u, dist[u]))

        return dist, parent
    print(dijkstra(G,0))
    return 0

runtests ( lufthansa, all_tests=False)