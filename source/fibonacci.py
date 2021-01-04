d = {0: 1, 1: 1}
# python evaluates expressions left to right
def fibonacci(n, d):
    """
    input: n an int >= 0
    output: nth Fibonacci number
    """
    if n in d:
        return d[n]
    else:
        x = fibonacci(n-2, d) + fibonacci(n-1, d) 
        d[n] = x
        return  x

print(fibonacci(100, d), d)