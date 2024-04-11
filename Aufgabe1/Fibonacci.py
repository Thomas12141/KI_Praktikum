def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    if n == 0:
        return 0
    n_minus_one_element = 1
    n_element = 1
    for i in range(2, n):
        temp = n_element
        n_element = n_minus_one_element + n_element
        n_minus_one_element = temp
    return n_element


print(fibonacci_recursive(13))
