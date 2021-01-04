def bubble_sort(L): 
    """
    input: unsorted list L
    output: sorted list L
    n^2 bubble sort implementation
    """
    swaps = True
    while swaps is True:
        swaps = False
        for i in range(1, len(L)):
            if L[i-1] > L[i]:
                temp = L[i-1]
                L[i-1] = L[i]
                L[i] = temp
                swaps = True
    return L

print(bubble_sort([5,4,3,2,1]))
