from egzP2atesty import runtests 

def zdjecie(T, m, k):
    Tnew=T.copy()

    Tnew.sort(key=lambda x:x[1])
    Tnew.reverse()
    n=len(T)
    triangle=(m*(m-1))/2
    counter=k
    lines=0
    counter2=0
    diff=2
    #if n>100:
    #    return 0
    for i in range(n):
        if counter>=0:
            #print(n,lines+m*counter2,counter)
            T[lines+m*counter2]=Tnew[i]
            counter2+=1
            counter-=1
        else:
            #print(lines+(counter2-1)*m+(m+counter))
            T[lines+(counter2-1)*m+(m+counter)]=Tnew[i]
            counter-=1
        if m+counter<diff:
            diff+=1
            counter=k
            lines+=1
            counter2=0
    return None


runtests ( zdjecie, all_tests=False )