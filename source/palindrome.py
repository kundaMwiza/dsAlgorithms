def for_palindrome(string):
    """
    input: string
    output: True if palindrome, False o/w
    implemented with a for loop
    """
    for i, ch in enumerate(string):
        if ch != string[-i-1]:
            return False
    return True

def rec_palindrome(string):
    """
    input: string
    output: True if palidrome, False o/w
    implemented with recursion
    """
    string = string.lower()
    n = len(string)
    start = 0
    stop = n-1
    def is_palindrome(string, stop, start):
        if stop == start:
            return True
        elif (stop - start) == 1 or (stop - start) == 2:
            return string[start] == string[stop]
        else:
            x = string[start] == string[stop]
            return x and is_palindrome(string, stop-1, start+1)
    return is_palindrome(string, stop, start)

print(rec_palindrome('ara'))
        


 
