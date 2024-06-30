from egzP4atesty import runtests 

def mosty ( T ):
    n=len(T)
    T.sort(key = lambda x : (x[0],x[1]))
    maxval=[0 for i in range(n)]
    maxval[0]=1
    for i in range(1,n):
        currmax=0
        for j in range(i):
            if T[j][1]<T[i][1] and currmax<maxval[j]:
                currmax=maxval[j]
            maxval[i]=currmax+1

    return max(maxval)

runtests ( mosty, all_tests=True)