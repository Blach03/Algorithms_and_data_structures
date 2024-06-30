#Błażej Kapkowski
#Używamy algorytmu dfs aby znalesc najkrótszą scieżkę pomiedzy wyznaczonymi punktami oraz zwracamy dlugość tej ścieżki oraz rodzica każdego odwiedzonego wierzchołka.
#Dzieki tablicy rodziców cofamy się od ostatniego wierzchołka i odwzorowujemy ścieżkę.
#Nastepnie usuwamy pokolej krawędzie ze ścieżki i sprawdzamy czy długość najkrótszej ścieżki się zwiekszyla, jeśli tak to zwracamy usuniętą krawędź.
#Algorytm dfs ma złożoność O(V+E) wykonujemy ją raz żeby uzyskać rodziców oraz n razy podczas sprawdzania długości gdzie n to długość najkrótszej ścieżki,
#która w najgorszym przypadku ma długość V-1. Zatem złożoność to O((V-1+1)*(V+E)) = O(V(V+E))
from zad4testy import runtests
from collections import deque

def dfs(G, s, t):
    Q = deque()
    n = len(G)
    dist = [-1]*n
    visited = [False]*n
    parent = [None]*n
    Q.append(s)
    dist[s] = 0
    while Q:
        u = Q.popleft()
        for neighbour in G[u]:
            if not(visited[neighbour]):
                dist[neighbour] = dist[u]+1
                parent[neighbour] = u
                visited[neighbour] = True
                Q.append(neighbour)
                if neighbour == t:
                    return dist[neighbour], parent
    return None, None


def longer(G, s, t):
    prev = dfs(G, s, t)[1]
    if prev is None:
        return None
    path = []
    v = t
    while v != s:
        u = prev[v]
        path.append((u, v))
        v = u
    path.reverse()
    min_len = len(path)
    for edge in path:
        p = edge[0]
        q = edge[1]
        G[p].remove(q)
        G[q].remove(p)
        new_len = dfs(G, s, t)[0]
        if new_len is None:
            return (p, q)
        if new_len > min_len:
            return (p, q)

        G[p].append(q)
        G[q].append(p)

    return None

runtests( longer, all_tests = True )