#Błażej Kapkowski
#Na początku algorytm zamienia listę krawędzi na listę sąsiedztwa
#Następnie, żeby ograniczyć ilość rozważanych przypadków, sprawdzamy wszystkie wysokości na krawędziach przy początku i końcu lotu i jeżeli w grafie znajdziemy krawędź, która jest za mała lub za duża to ją usuwamy
#Następnie znajdujemy najkrótszą scieżkę od początku do końca i sprawdzamy czy jest ona odpowiednia. Jeśli tak to zwracamy true a jeśli nie to sprawdzamy, która krawędź w ścieżce nie pozwala nam dolecieć do końca i usuwamy tą krawędź z grafu
#Powtarzamy to dopóki nie znajdziemy ścieżki, która jest prawidłowa albo do momentu gdy nie będzie istnieć żadna ścieżka łącząca początek z końcem, w takim przypadku zwracamy False.
#Do znajdowania śćieżki używamy algorytmu djikstry który ma złożoność ElogV jednak możemy ten algorytm wykonywać kilkukrotnie w niektórych przypadkach, w najgorszym przypadku wykonamy go aż E razy
#Zatem algorytm ma złożoność O(E^2logV) jednak w znacznej wiekszości przypadków algorytm djikstry wokona się maksymalnie kilkukrotnie więc lepszym określeniem złożoności może być O(ElogV)


from zad4testy import runtests


def Flight(L, x, y, t):
    def edges_to_adjacency_list(L):
        adjacency_list = [[] for _ in range(max(max(u, v) for u, v, _ in L) + 1)]
        for u, v, p in L:
            adjacency_list[u].append((v, p))
            adjacency_list[v].append((u, p))
        return adjacency_list

    def shortest_path(start, end):
      costs = [float('inf')] * len(G)
      predecessors = [-1] * len(G)
      costs[start] = 0

      queue = [(0, start)]

      while queue:
          cost, node = min(queue)

          if node == end:
              path = []
              while node != -1:
                  path.append(node)
                  node = predecessors[node]
              return path[::-1]

          queue.remove((cost, node))

          for neighbor, weight in G[node]:
              new_cost = costs[node] + weight
              if new_cost < costs[neighbor]:
                  costs[neighbor] = new_cost
                  predecessors[neighbor] = node
                  queue.append((new_cost, neighbor))

      return None
    
    G = edges_to_adjacency_list(L)

    minn = float('inf')
    maxx = 0
    for el in G[x]:
      minn = min(el[1] - 2*t, minn)
      maxx = max(el[1] + 2*t, maxx)

    for v in G:
      for e in v:
        if e[1] > maxx or e[1] < minn:
          v.remove(e)
         

    minn = float('inf')
    maxx = 0

    for el in G[y]:
      minn = min(el[1] - 2*t, minn)
      maxx = max(el[1] + 2*t, maxx)

    for v in G:
      for e in v:
        if e[1] > maxx or e[1] < minn:
          v.remove(e)
          

    path = shortest_path(x, y)
    if path == None:
      return False
    minn = float('inf')
    maxx = 0

    for i in range(len(path)-1):
      for el in G[path[i]]:
        if el[0] == path[i+1]:
          minn = min(el[1], minn)
          maxx = max(el[1], maxx) 


    def remove(path, t):
      removed = False
      minn = float('inf')
      maxx = 0
      for i in range(len(path)-1):
        for el in G[path[i]]:
          if el[0] == path[i+1]:
            minn = min(el[1], minn)
            maxx = max(el[1], maxx)
            for el2 in G[path[i+1]]:
              if el2[0] == path[i]:
                other = el2
            if (maxx - minn) / 2 > t:
              G[path[i]].remove(el)
              G[path[i+1]].remove(other)
              removed = True
      return removed
    
    if (maxx - minn) / 2 > t:
      removed = True
      while removed:
        removed = remove(path, t)
        path = shortest_path(x, y)
        if path == None:
          return False
        minn = float('inf')
        maxx = 0

        for i in range(len(path)-1):
          for el in G[path[i]]:
            if el[0] == path[i+1]:
              minn = min(el[1], minn)
              maxx = max(el[1], maxx) 

        if (maxx - minn) / 2 < t:
          return True
      return True
    return True

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
