def insertion_sort(input_arr):
    """
    function sorting an array of n numbers using the
    insertion sort algorithm
    input: array of length n (n >= 2)  
    output: nondecreasing array of length n 
    """
    for i in range(1, len(input_arr)):
        key = input_arr[i]
        j = i-1 
        while j >= 0 and input_arr[j] > key:
            input_arr[j+1] = input_arr[j]
            j -= 1 
        input_arr[j+1] = key

    return input_arr

if __name__ == '__main__':
    input_arr = [5,25,5,3,1]
    print("input array:", input_arr)
    print("insertion sorted array:", insertion_sort(input_arr))
    
