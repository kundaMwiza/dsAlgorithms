def insertion_sort(array, inc):
    # return nondecreasing sorted array
    if inc:
        print(len(array))
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            print(i, key)
            while j > - 1 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
    # return nonincreasing sorted array
    else:
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j > - 1 and key > array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
    
    return array
        
        
if __name__ == "__main__":
    test_array = [25,34,56,2,5,71,3]
    print(insertion_sort(test_array, False))