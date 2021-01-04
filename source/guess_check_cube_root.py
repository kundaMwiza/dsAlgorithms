cube = 8
code_sec = 'bisec_search'

"""-------------------naive code---------------------------"""
if code_sec == 'naive_soln':
    for guess in range(abs(cube)+1):
        if guess**3>=abs(cube):
            break
    if guess**3 != abs(cube):
        print(cube, 'is not a perfect cube')
    else:
        if cube <= 0:
            guess *= -1
        print('Cube root of', cube, 'is', guess)

"""------------------- approximate soln---------------------"""
if code_sec == 'apr_soln':
    guess = 0
    eps = 0.01
    increment = 0.001
    num_guesses = 0

    while abs(guess**3 - cube) > eps and abs(guess**3) <= abs(cube):
        print(guess**3)
        if (guess**3 - cube) < 0:
            guess += increment
        else:
            guess -= increment
        num_guesses += 1
    print('Number of guesses:',num_guesses, 'approximate soln:', guess)
    
"""------------------- bisec_search---------------------"""
# log_2 N = number of guesses
# halves the search space from 0 - N in each iteration
if code_sec == 'bisec_search':
    eps = 0.01
    guess = cube
    upper_bound = cube
    lower_bound = 0
    num_guesses = 1
    while abs(guess**3 - cube) > eps:
        if guess**3 - cube > 0:
            upper_bound = guess
        else:
            lower_bound = guess
        guess = 0.5 * (upper_bound + lower_bound)
        num_guesses += 1
    print('Number of guesses', num_guesses, 'apx soln', guess)
