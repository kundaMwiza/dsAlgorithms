def bisect_search(L, e):
    """
    input: sorted list L
    output: True if item found, False o/w
    log(n) recursive implementation of bisection search
    """
    def bisect_search_helper(L, low, high, e):
        if low == high:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        if L[mid] > e:
            if low == mid:
                return False
            else:
                return bisect_search_helper(L, low, mid - 1, e)
        else:
                return bisect_search_helper(L, mid+1, high, e)
    if len(L) == 0:
        return False
    return bisect_search_helper(L, 0, len(L)-1, e)

print(bisect_search([1,2,3,4,5], 3))
