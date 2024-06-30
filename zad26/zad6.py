#Błażej Kapkowski
#Tworzymy tablicę trójwymiarową dist o wymiarach n x 2 x n, gdzie n to liczba wierzchołków.
#dist[v][boots_used][prev] przechowuje najkrótszą odległość do wierzchołka v używając boots_used liczby "dwumilowych butów", poprzednio przetwarzając prev.
#Kolejka priorytetowa pq przechowuje cztery wartości (d, u, boots_used, prev), gdzie d - bieżąca odległość, u - obecny wierzchołek, boots_used - czy buty zostały użyte, prev - poprzedni wierzchołek.
#Używamy kolejki priorytetowej (heapq), aby zawsze przetwarzać węzeł o najkrótszej obecnie znanej ścieżce.
#Algorytm aktualizuje odległość do każdego węzła, jeśli nowo znaleziona ścieżka jest krótsza i uwzględnia w tym czy buty były użyte czy też nie.
#Algorytm ma złożoność O(n^2logn) ponieważ posiadamy tablice dist która ma rozmiary n x 2 x n czyli (n^2) oraz dla każdej krawędzi, których jest maxymalnie n^2 w grafie pełnych, wykonujemy operacje na kopcu, które mają złożoność O(logn)

from zad6testy import runtests

import heapq

def jumper(G, s, w):
    n = len(G)
    inf = float('inf')
    dist = [[[inf for _ in range(n)] for _ in range(2)] for _ in range(n)]
    pq = []
    
    dist[s][0][s] = 0
    heapq.heappush(pq, (0, s, 0, s))
    
    while pq:
        d, u, boots_used, last = heapq.heappop(pq)
        
        if u == w:
            return d
        
        if d > dist[u][boots_used][last]:
            continue
        
        for v in range(n):
            if G[u][v] == 0:
                continue
            
            new_d = d + G[u][v]
            
            if dist[v][0][u] > new_d:
                dist[v][0][u] = new_d
                heapq.heappush(pq, (new_d, v, 0, u))
            
            if boots_used == 0:
                for v2 in range(n):
                    if G[v][v2] == 0 or v2 == u:
                        continue
                    
                    new_d_boot = d + max(G[u][v], G[v][v2])
                    
                    if dist[v2][1][u] > new_d_boot:
                        dist[v2][1][u] = new_d_boot
                        heapq.heappush(pq, (new_d_boot, v2, 1, u))
    
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )