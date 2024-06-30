"""from zad7testy import runtests


def maze(L):
    print(L)
    n=len(L)
    tab=[[-1]*n for _ in range(n)]
    visited=[[False]*n for _ in range(n)]
    tab[0][0]=0
    maks=0
    def fill(x,y,move):
        nonlocal maks,visited
        n=len(L)
        if x<0 or x>=n or y<0 or y>=n or L[x][y]=='#' or visited[x][y]:
            return 0

        if move==0:
            val=tab[x-1][y]
        if move==1:
            val=tab[x+1][y]
        if move==2:
            val=tab[x][y-1]
        print(val,tab[x][y],x,y)
        if visited[x][y] and (tab[x][y]>val):
            return 0

        print(x,y)
        if x==y and x==n-1:
            print("aaaaaaaaaa")
            if tab[x][y]>maks:
                maks=tab[x][y]
            visited = [[False] * n for _ in range(n)]

        a=b=c=-1
        if x>0:
            a=tab[x-1][y]+1
        if x<n-1:
            b=tab[x+1][y]+1
        if y>0:
            c=tab[x][y-1]+1
        visited[x][y] = True
        tab[x][y]=max(a,b,c)
        if x<n-1 and move!=1:
            if visited[x+1][y] and tab[x+1][y]<tab[x][y]+1:
                visited[x+1][y]=False
            fill(x+1,y,0)

        if x>0 and move!=0:
            if visited[x-1][y] and tab[x-1][y]<tab[x][y]+1:
                visited[x-1][y]=False
            fill(x-1,y,1)
        if y<n-1:
            if visited[x][y+1] and tab[x][y+1]<tab[x][y]+1:
                visited[x][y+1]=False
        fill(x,y+1,2)

    fill(0,0,0)
    for i in tab:
        print(i)
    return tab[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = False )
"""
from zad7testy import runtests


def maze(L):
    n = len(L)

    # Initialize DP tables for upward and downward paths
    dp_up = [[-1]*n for _ in range(n)]
    dp_down = [[-1]*n for _ in range(n)]

    # Start from the top left room
    dp_up[0][0] = 1 if L[0][0] == '.' else -1

    # Process column by column
    for col in range(n):
        # Upward pass
        for row in range(n):
            if L[row][col] == '#':
                continue
            if row > 0 and dp_up[row-1][col] != -1:
                dp_up[row][col] = max(dp_up[row][col], dp_up[row-1][col] + 1)
            if col > 0 and dp_up[row][col-1] != -1:
                dp_up[row][col] = max(dp_up[row][col], dp_up[row][col-1] + 1)

        # Downward pass
        for row in range(n-1, -1, -1):
            if L[row][col] == '#':
                continue
            if row < n-1 and dp_down[row+1][col] != -1:
                dp_down[row][col] = max(dp_down[row][col], dp_down[row+1][col] + 1)
            if col > 0 and dp_down[row][col-1] != -1:
                dp_down[row][col] = max(dp_down[row][col], dp_down[row][col-1] + 1)

        # Combine upward and downward paths for the next column
        if col < n-1:
            for row in range(n):
                if dp_up[row][col] != -1 or dp_down[row][col] != -1:
                    dp_up[row][col+1] = dp_down[row][col+1] = max(dp_up[row][col], dp_down[row][col]) + 1 if L[row][col+1] == '.' else -1

    res = max(dp_up[n-1][n-1], dp_down[n-1][n-1])
    return res if res == -1 else res - 1





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )