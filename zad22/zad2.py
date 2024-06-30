#Błażej Kapkowski
#Na początku implementujemy kopiec oraz quicksorta, które przydadzą nam sie w głównej funkcji
#Algorytm rozpoczyna od utworzenia 2 kopców które przechowują wsumie p elementów pierwszy kopiec przechowuje k najwiekszych a drugi reszte
#k- ta najwieksza wartość bedzie zawsze przechowywana na szyscie kopca max_heap.
#Przechodzimy przedziałem p po calej tablicy w taki sposób że dodajemy 1 element do kopców i usuwamy wa każdej iteracji
#dodany element jest dodawany do odpowiedniego kopca i kopce są aktualizowane w taki sposób aby max_heap dalej posiadał k wartości, tak samo robimy usuwając 1 element
#po każdym przejści dodajemy aktualną k-tą najwiekszą wartosc do wyniku
# algorytm ma złożoność O(nlogn) poniważ quicksort ma złożoność nlogn oraz przechodzimy przedziałem po całej liści która ma n wyrazów oraz operacje na kopcach, 
#które wykonujemy podczas każdej iteracji mają złożoność logn.


from zad2testy import runtests


def heappop(heap):
    last_element = heap.pop()
    if heap:
        return_item = heap[0]
        heap[0] = last_element
        _sift_down(heap, 0)
        return return_item
    return last_element

def heappush(heap, item):
    heap.append(item)
    _sift_up(heap, len(heap) - 1)

def heapify(heap):
    n = len(heap)
    for i in reversed(range(n // 2)):
        _sift_down(heap, i)

def _sift_up(heap, index):
    parent_index = (index - 1) // 2
    while index > 0 and heap[index] < heap[parent_index]:
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        index = parent_index
        parent_index = (index - 1) // 2

def _sift_down(heap, index):
    child_index = 2 * index + 1
    while child_index < len(heap):
        if child_index + 1 < len(heap) and heap[child_index + 1] < heap[child_index]:
            child_index += 1
        if heap[child_index] < heap[index]:
            heap[child_index], heap[index] = heap[index], heap[child_index]
            index = child_index
            child_index = 2 * index + 1
        else:
            break

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def ksum(T, k, p):
    n = len(T)

    sub = T[:p]
    sub = quicksort(sub)

    max_heap = []
    heap2 = []
    for i in range(p-k):
        heappush(heap2, -sub[i])

    for j in range(i+1,p):
        heappush(max_heap, sub[j])
    
    #print(max_heap)
    #print(heap2)
    
    result = max_heap[0]
    
    for i in range(n - p):
        heappush(heap2, -T[i+p])
        #print(max_heap, heap2, T[i])
        if -T[i] in heap2:
            heap2.remove(-T[i])
            heapify(heap2)
            transfer = heappop(max_heap)
            heappush(heap2, -transfer)
            transfer = -heappop(heap2)
            heappush(max_heap, transfer)
        else:
            max_heap.remove(T[i])
            heapify(max_heap)
            transfer = -heappop(heap2)
            heappush(max_heap, transfer)

        #print(max_heap[0])
        #print(max_heap, heap2)
        result += max_heap[0]

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )






"""
def ksum(T, k, p):
    n = len(T)

    sub = T[:p]
    sub.sort()

    max_heap = []
    heap2 = []
    for i in range(p-k):
        heapq.heappush(heap2, -sub[i])

    for j in range(i+1,p):
        heapq.heappush(max_heap, sub[j])
    
    #print(max_heap)
    #print(heap2)
    
    result = max_heap[0]
    
    for i in range(n - p):
        heapq.heappush(heap2, -T[i+p])
        #print(max_heap, heap2, T[i])
        if -T[i] in heap2:
            heap2.remove(-T[i])
            heapq.heapify(heap2)
            transfer = heapq.heappop(max_heap)
            heapq.heappush(heap2, -transfer)
            transfer = -heapq.heappop(heap2)
            heapq.heappush(max_heap, transfer)
        else:
            max_heap.remove(T[i])
            heapq.heapify(max_heap)
            transfer = -heapq.heappop(heap2)
            heapq.heappush(max_heap, transfer)

        #print(max_heap[0])
        #print(max_heap, heap2)
        result += max_heap[0]

    return result

"""