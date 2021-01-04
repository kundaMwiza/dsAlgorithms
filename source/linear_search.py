def linear_search(array, value):
    index = None
    for i in range(len(array)):
        # value found
        if array[i] == value:
            print("value found in array, matching index is:", i + 1 )
            index = i + 1
            return index =i + 1
    # value not found
    print("value not found in array")
    return index

if __name__ == "__main__":
    test_array = [1,3,6,345,3]
    linear_search(test_array, 5)