primes = []

i = 1
while True:
    i += 1
    for d in range(2,i):
        if i % d == 0: break
    else:
        primes.append(i)
        print(i)