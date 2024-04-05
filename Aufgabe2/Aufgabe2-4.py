def factorial_n_plus_one(n):
    factorials = []
    result = 1
    for i in range(2, n + 2):
        result *= i
        factorials.append(result)
    for j in range(len(factorials)):
        yield "a" + str(len(factorials) - j) + " = " + str(factorials[len(factorials) - j - 1])


number = int(input("Enter an integer: "))
for n in factorial_n_plus_one(number):
    print(n)
