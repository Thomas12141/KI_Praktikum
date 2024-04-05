def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    prev_fib = 0
    fib = 1
    for i in range(n-1):
        temp = fib
        fib = fib + prev_fib
        prev_fib = temp
    return fib


print(fibonacci_iterative(7))
