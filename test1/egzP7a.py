from egzP7atesty import runtests 

def akademik( T ):

    def match(v):
        if visited[v]:
            return False
        visited[v] = True
        for u in M[v]:
            if matched[u] is None or match(matched[u]):
                matched[u] = v
                return True
        return False
    full=[i for i in range(len(T))]
    M=[[] for _ in range(len(T))]
    for i in range(len(T)):
        if T[i]==(None,None,None):
            M[i]=full
        else:
            for el in T[i]:
                if el!=None:
                    M[i].append(el)
    print(M)
    n = len(M)
    matched = [None] * n
    for i in range(n):
        visited = [False] * n
        match(i)

    result = 0
    for i in matched:
        if i is not None:
            result += 1
    return n-result


runtests ( akademik )