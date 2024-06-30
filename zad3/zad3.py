#Błażej Kapkowski
#Na początku program przechodzi przez wszystkie elementy tablicy i odwraca te których pierwsza litera jest mniejsza od ostatniej
#W taki sposób pozbędziemy się napisów równoważnych i staną się identyczne w przypadku takich samych liter na początku i końcu
#sprawdza także kolejne litery. Jest to podwójna zagnieżdżona pętla jednak przejdzie ona maksymalnie po każdej literze tablicy 1 raz
#zatem jej złożoność nie przekroczy N. Następnie otrzymane napisy sortujemy przy użyciu quicksorta z wybieraniem losowego pivota
#Teraz wystarczy zliczyć maksymalną ilość takich samych napisów stojących obok siebie i zwrócić tą wartość.
#Złożoność programu to bedzie O(N + nlog n) ponieważ przy odwracaniu słów przejdziemy przez każdą literę maxymalnie raz oraz quicksort
#ma złożoność nlog n w przypadku wybierania losowego pivota.

from zad3testy import runtests

def strong_string(T):
    from random import randint
    n=len(T)
    for i in range(n):
        if ord(T[i][0])>ord(T[i][-1]):
            T[i]=T[i][::-1]
        if ord(T[i][0])==ord(T[i][-1]):
            k=len(T[i])
            j=0
            while ord(T[i][j])==ord(T[i][k-1-j]) and j<k//2:
                j+=1
            if ord(T[i][j]) > ord(T[i][k-1-j]):
                T[i] = T[i][::-1]

    def partition(A, p, r):
        a = randint(p, r)
        A[a], A[r] = A[r], A[a]
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def quicksort(A, p, r):
        while p < r:
            q = partition(A, p, r)
            quicksort(A, p, q - 1)
            p = q + 1

    quicksort(T,0,n-1)
    max_value=0
    curr_value=0
    prev=""
    for i in range(n):
        if prev==T[i]:
            curr_value+=1
        else:
            if curr_value>max_value:
                max_value=curr_value
            curr_value=1
        prev=T[i]
    return max_value


runtests( strong_string, all_tests=True )
