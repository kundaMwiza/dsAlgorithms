def selection_sort(L):
    """
    input: unsorted list L
    output: sorted list 
    O(n^2) implementation of selection sort
    """
    sfx = 0
    list_len = len(L)
    while sfx != list_len:
        for i in range(sfx, list_len):
            if L[sfx] > L[i]:
                temp = L[sfx]
                L[sfx] = L[i]
                L[i] = temp
        sfx += 1
    return L

print(selection_sort([5, 4, 3, 2, 1]))