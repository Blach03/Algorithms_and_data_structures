from zad7testy import runtests

i=0
def maze( L ):
    n = len(L)
    
    # Tablica dp[x][y] oznacza maksymalną liczbę komnat, które można odwiedzić,
    # przybywając do komnaty (x, y)
    dp = [[[-1] * 3 for _ in range(n)] for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    dp[0][0] = [0, 0, 0]
    
    # Funkcja pomocnicza do sprawdzenia, czy można odwiedzić komnatę (x, y)
    def can_visit(x, y):
        return 0 <= x < n and 0 <= y < n and L[x][y] == '.' and not visited[x][y]

    # Funkcja rekurencyjna do obliczania maksymalnej liczby odwiedzonych komnat
    def calculate(x, y):

        print(x,y)
        for line in dp:
            print(line)
        
        visited[x][y] = True

        if dp[x][y] != [-1, -1, -1]:
            return dp[x][y]
        
        max_visited = [-1, -1, -1]
        
        # Możliwe ruchy: prawo, dół, góra
        if can_visit(x, y - 1):  # ruch w prawo
            result = calculate(x, y - 1)
            print(result,"left", x, y)
            max_visited[0] = max(max_visited[0], 1 + max(result))
        
        if can_visit(x + 1, y):  # ruch w dół
            result = calculate(x + 1, y)
            print(result, "up", x, y)
            max_visited[1] = max(max_visited[1], 1 + max(result))
        
        if can_visit(x - 1, y):  # ruch w górę
            result = calculate(x - 1, y)
            print(result, "down", x, y)
            max_visited[2] = max(max_visited[2], 1 + max(result))
        
        print(max_visited, "vis", x, y)
    
        
        dp[x][y] = max_visited
        visited[x][y] = False
        return max_visited
    
    # Inicjujemy rekurencję z pozycji startowej
    result = calculate(n-1, n-1)
    result = max(result)
    print(dp)
    return result if result != -1 else -1

print(maze(['....', '..#.', '..#.', '....']))
# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( maze, all_tests = False )
