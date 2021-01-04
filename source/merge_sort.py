def merge_sort(L):
    """
    input: unsorted list L
    output: sorted list L 
    """
    def merge_two(left, right):
        ind_left = 0
        ind_right = 0 
        result = []
        while ind_left != len(left) and ind_right != len(right):
            print(left, right, result, ind_left, ind_right)
            if left[ind_left] > right[ind_right]:
                result.append(right[ind_right])
                ind_right += 1 
            elif left[ind_left] == right[ind_right]:
                result.append(left[ind_left])
                result.append(right[ind_right])
                ind_left += 1
                ind_right += 1
            else:
                result.append(left[ind_left])
                ind_left += 1
        if ind_left == len(left)-1:
            result += left[ind_left:]
        else:
            result += right[ind_right:]
        return result
             
    def merge_sort_helper(subL):
        if len(subL) == 1:
            return subL
        else:
            mid = len(subL)//2
            left = merge_sort_helper(subL[:mid])
            right = merge_sort_helper(subL[mid:])
            result = merge_two(left, right)
            return result

    return merge_sort_helper(L)

print(merge_sort([1,2,3,4,5,6]))
