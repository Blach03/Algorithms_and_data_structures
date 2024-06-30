from egzP5atesty import runtests 

def inwestor ( T ):
    n=len(T)
    if len(T)<100: print(T)
    maxx=0
    for j in range(n):
        maxsum=T[j]
        minn=T[j]
        for i in range(1,n):
            left=j-i
            if left<0: left=0
            right=j+i
            if right>n-1: right=n-1
            leftval=rightval=-1
            if j - i >= 0:
                leftval=T[j-i]
            if j + i < n:
                rightval=T[j+i]
            if leftval>rightval:
                if j - i >= 0:
                    if T[j - i] < minn: minn = T[j - i]
                leng = right - left
                currsum = leng * minn
                if currsum > maxsum: maxsum = currsum
                if j + i < n:
                    if T[j + i] < minn: minn = T[j + i]
                leng = right - left+1
                currsum = leng * minn
                if currsum > maxsum: maxsum = currsum
            else:
                if j + i < n:
                    if T[j + i] < minn: minn = T[j + i]
                leng = right - left
                currsum = leng * minn
                if currsum > maxsum: maxsum = currsum
                if j - i >= 0:
                    if T[j - i] < minn: minn = T[j - i]
                leng = right - left+1
                currsum = leng * minn
                if currsum > maxsum: maxsum = currsum


        if maxx<maxsum: maxx=maxsum

    return maxx

runtests ( inwestor, all_tests=True )