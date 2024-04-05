import functools


def factorial_n_plus_one(n):
    factorials = []
    result = 1
    for i in range(2, n + 2):
        result *= i
        factorials.append(result)
    for j in factorials:
        yield j


number = int(input("Enter an integer: "))
numbers = factorial_n_plus_one(number)
results = []
for number in numbers:
    results.append(number)

print(str(int(functools.reduce(lambda x, y: (x+y), results)/len(results))))
