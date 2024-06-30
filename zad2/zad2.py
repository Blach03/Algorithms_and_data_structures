from zad2testy import runtests

def snow( S ):
    n = len(S)
    maks=max(S)
    left=0
    right=0
    suma=0
    tab=[[i,S[i]] for i in range(n)]
    while left+right<n:
        i=0
        j=0
        tab_left=[]
        tab_right=[]
        while i*2<maks and i+left<n:
            tab_left.append([left+i,S[left+i]-2*i])
            i+=1
            
        while j*2<maks and j+right<n:
            tab_right.append([n-1-right-j,S[n-1-right-j]-2*j])
            j+=1
         
        
        tab_left.sort(key=lambda x: x[1], reverse=True)
        tab_right.sort(key=lambda x: x[1], reverse=True)
        if tab_left[0][1]>tab_right[0][1]:
            index=tab_left[0][0]
            left=index+1
        else:
            index=tab_right[0][0]
            right=n-index
        suma+=S[index]
        S[index]=0
        
        
        while S[left]<2:
            left+=1
            if left+right>=n:
                return suma
        while S[n-1-right]<2:
            right+=1
            if left+right>=n:
                return suma
        
        for i in range(left, n-right):
            if S[i]!=0:
                S[i]-=1
        maks-=1
        
    
    return suma

runtests( snow, all_tests = False )
