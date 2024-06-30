#Błażej Kapkowski
#Zaczynamy od zamienienia listy krawędzi na liste sąsiadów gdzie sąsiadzem jest krotka składająca się z numeru wierzchołka i odległości do tego wierzchołka.
#Następnie dodajemy połączenia pomiedzy każdą osobliwością z odległością 0
#Używając algorytmu dijkstry zwracamy najkrótszą odległość
#Przekształcenie listy jest liniowe a algorytm dijkstryu ma złożoność O(ElogV) zatem algorytm ma złożoność O(ElogV)
#Jednak w szczególnych przypadkach gdy każdy wierzchołek jest osobliwością to dodawanie krawędzi pomiedzy osobliwościami będzie miało złożoność O(V^2)

from zad5testy import runtests

from queue import PriorityQueue

def dijkstra(G, s, t):
    n = len(G)
    dist = [float('inf')]*n
    dist[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        u = Q.get()[1]
        if u == t:
            break
        for v in G[u]:
            new_dist = dist[u] + v[1]                             
            if new_dist < dist[v[0]]:
                dist[v[0]] = new_dist
                Q.put((dist[v[0]], v[0]))

    if dist[t] == float('inf'):
        return None

    return dist[t]

def spacetravel( n, E, S, a, b ):
    G = [[] for _ in range(n)]
    for v1, v2, weight in E:
        G[v1].append((v2, weight))
        G[v2].append((v1, weight))
    k = len(S)

    for i in range(k):
        for j in range(i + 1, k):
            G[S[i]].append((S[j], 0))
            G[S[j]].append((S[i], 0))

    return dijkstra(G, a, b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )