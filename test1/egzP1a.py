from egzP1atesty import runtests

def titanic( W, M, D ):
    if len(W)>100:
        return 0
    text=''
    for letter in W:
        for let in M:
            if let[0]==letter:
                code=let[1]
                break
        text+=code

    letters=[]
    for i in D:
        letters.append(M[i][1])
    print(letters)
    print(text)
    n=len(text)
    tab=[float('inf') for _ in range(n)]
    tab[0]=1
    used=[0 for _ in range(n)]
    for i in range(1,n):
        values=[]
        if i>=3:
            print(text[i-3:i+1])
            if text[i-3:i+1] in letters:
                if not used[i - 3]:
                    print("a")
                    values.append(tab[i-3])
        if i>=2:
            print(text[i-2:i+1])
            if text[i-2:i+1] in letters:
                if not used[i-2]:
                    print("b")
                    values.append(tab[i-2])

        print(text[i-1:i+1])
        if text[i-1:i+1] in letters:
            if not used[i-1]:
                print("c")
                values.append(tab[i-1])
        values.append(tab[i-1]+1)
        if len(values)>1:
            used[i]=1
        tab[i]=min(values)
        print(tab)
    print(W)
    print(M)
    print(D)

    return tab[-1]

runtests ( titanic, recursion=False )