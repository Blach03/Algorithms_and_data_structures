#Błażej Kapkowski
#Algorytm rozpoczyna od zliczenia wartości każdego złoża ropy który ma dostęp do powierzchni.
#Zapisuje otrzymane wyniki w tablicy oraz indeksy tablicy w którym poraz pierwszy pojawiło się to złoże.
#Następnie tworzy nową drogę jednowymiarową z wartościami całego złoża w jego pierwszym dostępie do powierzchni.
#Jest to jednoznaczne z poprzednią tablicą ponieważ jeżeli całą wartość złoża ropy zapiszemy w miejscu jego pierwszego wystąpienia,
#to nie będzie to wpływało na ilość potrzebnych zatrzymań.
#Następnie używamy funkcji rekurnecyjnej, która rozważa wszystkie możliwości wyboru złóż ropy i zwraca minimalną wartość.
#Funkcja dfs ma maxymalnie złożoność m*n poniważ zapamiętuje odwiedzone pola,
#a funkcja rekurencyjna rozważająca wszystkie możliwośći 2^m. Zatem algorytm ma złożoność O(n*m+2^m)

from zad8testy import runtests


def plan(T):
    for u in T:
        print(u)
    def calculate_oil_patches(T):
        n = len(T)
        m = len(T[0])
        visited = [[False] * m for _ in range(n)]

        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < m and T[x][y] > 0 and not visited[x][y]

        def dfs(x, y):
            visited[x][y] = True
            val = T[x][y]
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if is_valid(new_x, new_y):
                    val += dfs(new_x, new_y)

            return val

        oil_patches = []
        index = []

        for i in range(m):
            if T[0][i] > 0 and not visited[0][i]:
                oil_patches.append(dfs(0, i))
                index.append(i)

        return oil_patches, index

    patches = calculate_oil_patches(T)
    new_road = [0]*len(T[0])
    for i in range(len(patches[0])):
        new_road[patches[1][i]] = patches[0][i]


    stops=1
    m = len(new_road)
    fuel = new_road[0]-1
    i=1
    while i<m:
        maks = new_road[i]
        maks_id = i
        if i+fuel>=m-1:
            break
        for j in range(1,fuel+1):
            if i+j<m:
                if new_road[i+j]>maks:
                    maks=new_road[i+j]
                    maks_id=i+j
        fuel=fuel-maks_id+i
        i=maks_id+1
        fuel+=new_road[maks_id]
        stops+=1


    return stops

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

