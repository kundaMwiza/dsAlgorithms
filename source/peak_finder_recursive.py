def peak_finder_recursive(L):
    """
    input: list of integers L
    output: peaks found, else no peaks found
    log(n) implementation of peak finding on a one-dimensional array
    """
    peaks = []
    if len(L) == 1:
        return peaks
    if len(L) == 2:
        if L[0] >= L[1]:
            peaks.append(L[0])
            return peaks
        peaks.append(L[1])
        return peaks
        
    def peak_finder_helper(low, high, L):
        index = (low + high)//2
        if index == 0:
            if L[0] >= L[1]:
                peaks.append((index, L[0]))
        elif index == len(L)-1:
            if L[-1] >= L[-2]:
                peaks.append((index, L[-1]))
        else:
            if L[index] < L[index+1]:
                peak_finder_helper(index+1, high, L)
            if L[index] < L[index-1]:
                peak_finder_helper(low, index-1, L)
            else:
                peaks.append((index, L[index]))

    peak_finder_helper(0, len(L), L)
    return peaks

print(peak_finder_recursive([1,4, 4, 4, 3]))
        