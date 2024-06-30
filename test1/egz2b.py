from egz2btesty import runtests

def parking(X,Y):
  def n2(X,Y):

    N, M = len(X), len(Y)

    dp = [[float('inf') for _ in range(M + 1)] for _ in range(N + 1)]

    for i in range(M):
      dp[0][i] = min(abs(X[0] - Y[i]), dp[0][max(0, i - 1)])

    for i in range(1, N):
      for j in range(i, M):
        dp[i][j] = min(dp[i - 1][j - 1] + abs(X[i] - Y[j]), dp[i][j - 1])

    print(f'Wynik: {min(dp[N - 1])}')


  def n3(X,Y):

    N, M = len(X), len(Y)

    dp = [[float('inf') for _ in range(M + 1)] for _ in range(N + 1)]

    for i in range(M):
      dp[0][i] = abs(X[0] - Y[i])

    for i in range(1, N):
      for j in range(i, M):
        min_prev = float('inf')
        for k in range(j):
          min_prev = min(min_prev, dp[i - 1][k])
        dp[i][j] = min_prev + abs(X[i] - Y[j])

    print(f'Wynik: {min(dp[N - 1])}')
  n2(X,Y)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
