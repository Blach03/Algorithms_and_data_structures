#Błażej Kapkowski
#Tworzymy tablice dp i prev_dp do przechowywania minimalnych kosztów anstępnie inisjalizujemy prev_dp dla pierwszego biurowca
#Nastepnie dla kazdej pozycji w dp szukamy minimalnej wartosci w prev_dp i zapisujemy ją do dp po dodaniu odległości
#Algorytm ma zlozoność O(n*m) 
from zad8testy import runtests

def parking(X, Y):
    n = len(X)
    m = len(Y)
    
    dp = [float('inf')] * m
    prev_dp = [float('inf')] * m
    
    for j in range(m):
        prev_dp[j] = abs(X[0] - Y[j])
    
    for i in range(1, n):
        min_prev = float('inf')
        for j in range(m):
            if j > 0:
                min_prev = min(min_prev, prev_dp[j-1])
            dp[j] = min_prev + abs(X[i] - Y[j])
        
        prev_dp, dp = dp, prev_dp

    return min(prev_dp)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
