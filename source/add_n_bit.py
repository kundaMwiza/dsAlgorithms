def add_n_bit(a, b):
    carry_over = 0
    c = []
    for i in range(len(a) - 1, -1, -1):
        quotient = (a[i] + b[i] + carry_over) // 2
        rem = (a[i] + b[i] + carry_over) % 2
        c.insert(0, rem)
        carry_over = quotient
    c.insert(0, carry_over)
    return c

print(add_n_bit([1,0,1,1,1], [0,1,1,0,1]))