#Błażej Kapkowski
#Algorytm rozpoczynamy od utworzenia tablicy dp do przechowywania najdluzszej sciezki z punktu (i, j)
#Następnie uzywamy dfs do znaleznienia wszystkich scieżek wychodzących z (i, j) i zwracamy tą która jest najdluzsza
#Używamy dfs do kazdego mozliwego punktu i zwracamy maxymalną wartość
#Każdą wartość w tablicy dp obliczamy tylko 1 raz więc algorytm ma złożoność O(n*m)
from zad9testy import runtests

def trip(M):
    n, m = len(M), len(M[0])
    dp = [[-1 for _ in range(m)] for __ in range(n)]
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j):
        if dp[i][j] != -1:
            return dp[i][j]
        
        max_path_length = 1 
        for dx, dy in directions:
            new_i, new_j = i + dx, j + dy
            if 0 <= new_i < n and 0 <= new_j < m and M[new_i][new_j] > M[i][j]:
                max_path_length = max(max_path_length, 1 + dfs(new_i, new_j))
        
        dp[i][j] = max_path_length
        return dp[i][j]

    longest_path = 0
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                longest_path = max(longest_path, dfs(i, j))

    return longest_path

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
