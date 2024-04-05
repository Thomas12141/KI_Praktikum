number = int(input("Enter an integer: "))
numbers = []
for i in range(number):
    numbers.append(i)
sequence = [(x+1)*2**(x+1) for x in numbers]

for i in range(len(sequence)):
    print("a" + str(len(sequence)-i) + " = " + str(sequence[len(sequence)-1-i]))
