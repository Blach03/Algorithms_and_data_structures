from egzP2btesty import runtests
from math import log10

def kryptograf( D, Q ):    
    n = len(D)
    sum=1
    for el in Q:
        if el=='':
            sum*=n
            continue
        curr=0
        for el2 in D:
            if len(el2)<len(el): continue
            k=len(el)
            if el2[-k:]==el: curr+=1
        sum*=curr
    sum=log10(sum)
    return sum

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
#runtests(kryptograf, all_tests = 1)

from random import randint
prev=1
numb=0
for i in range(1000000):
    if prev==0:
        x=1
    else:
        x=randint(0,1)
    prev=x
    numb+=x

print(numb)