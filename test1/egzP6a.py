from egzP6atesty import runtests 

def google ( H, s ):
    def number(a):

        if a=='0' or a=='1' or a=='2' or a=='3' or a=='4' or a=='5' or a=='6' or a=='7' or a=='8' or a=='9':
            return True
        return False
    weights=[(0,0,0)]*len(H)
    for i in range(len(H)):
        passwd=H[i]
        number_count=0
        for a in passwd:

            if number(a):
                number_count+=1
        weights[i]=(len(passwd),len(passwd)-number_count,i)
    weights.sort(key=lambda x: (x[0],x[1]), reverse=True)


    return H[weights[s-1][2]]


runtests ( google, all_tests=True )