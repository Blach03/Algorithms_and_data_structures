from zad3testy import runtests



def dominance(P):
    # Funkcja pomocnicza do scalania posortowanych podzbiorów
    def merge(left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i][1] > right[j][1]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    # Funkcja pomocnicza do zliczania dominujących punktów dla danego podzbioru
    def count_dominance(points):
        if len(points) <= 1:
            return points
        mid = len(points) // 2
        left = count_dominance(points[:mid])
        right = count_dominance(points[mid:])
        merged = merge(left, right)
        dominance_count = [0] * len(merged)
        max_dominance = 0
        for i in range(len(merged)-1, -1, -1):
            dominance_count[i] = max_dominance
            max_dominance = max(max_dominance, merged[i][1])
        return list(zip(merged, dominance_count))
    
    # Sortowanie punktów ze względu na współrzędne y
    sorted_points = sorted(P, key=lambda x: (x[0], -x[1]))
    # Liczenie dominujących punktów dla posortowanych punktów
    points_with_dominance = count_dominance(sorted_points)
    # Znalezienie najsilniejszego punktu
    max_strength = max(points_with_dominance, key=lambda x: x[0][1])[0][1]
    return max_strength


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = False )


"""def dominance(P):
    # Base case: if there are only two points left, compare them directly
    if len(P) <= 1:
        return 0

    # Divide the points into left and right subsets
    mid = len(P) // 2
    P_left = P[:mid]
    P_right = P[mid:]

    # Recursively count dominating pairs in left and right subsets
    count_left = dominance(P_left)
    count_right = dominance(P_right)

    # Count dominating pairs spanning across the division line
    i = j = 0
    count = 0
    while i < len(P_left) and j < len(P_right):
        if P_left[i][0] > P_right[j][0] and P_left[i][1] > P_right[j][1]:
            count += len(P_left) - i
            j += 1
        else:
            i += 1

    # Merge/Combine the results
    return count + count_left + count_right"""