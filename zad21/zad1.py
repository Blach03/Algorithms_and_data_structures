#Błażej Kapkowski
#Algorytm przechodzi po każdym elemencie listy i w zasięgu k szuka najmniejszej wartości. 
#Znalezioną wartość wstawia w jej odpowiednie miejsce i przechodzi do kolejnej pozycji w liście. 
#Algorytm ma złożoność O(nk) ponieważ posiada zagnieżdżone pętle o złożoności n i k. więc złożoność algorytmu zależy od k (dla k = O(1) ma złożoność O(n) a dla k = O(n) złożoność O(n^2))

from zad1testy import Node, runtests


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def SortH(p, k):
    curr = p

    while curr != None:
        minn = curr
        next = curr.next

        for i in range(k):
            if next == None:
                break
            if next.val < minn.val:
                minn = next
            next = next.next

        curr.val, minn.val = minn.val, curr.val
        curr = curr.next

    return p


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
