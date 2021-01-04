def pr_fr_to(fr, to):
    print('move one block from', fr, 'to', to)

def hanoi(n, fr, to, spare):
    if n == 1:
        pr_fr_to(fr, to)
    else:
        hanoi(n-1, fr, spare, to)
        hanoi(1, fr, to, spare)
        hanoi(n-1, spare, to, fr)