def isOdd(num):
    return (num % 2) != 0

for it in range(2, 50000):
    current = it
    steps = 0
    while current != 1:
        steps += 1
        if isOdd(current):
            current = (current * 3) + 1
        else:
            current = current / 2
    print("*" * steps)