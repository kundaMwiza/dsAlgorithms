def peak_finder_linear(L):
    """
    input: list of integers L
    output: peak element if it exists, else None
    O(n) implementation for the peak finding problem on a one dimensional array
    """
    for i in range(1,len(L)):
        if i == 1 and L[0] >= L[1]:
            return comp
        elif i == len(L)-1:
            if L[-1] >= L[-2]:
                return L[-1]
            return None
        else:
            if L[i] >= L[i-1] and L[i] >= L[i+1]:
                return L[i]

print(peak_finder([1,2,5,4,2]))

