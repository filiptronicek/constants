import atexit
import time

primes = []

def writeToFile():
    with open("outputs/primes.txt", "w") as f:
        f.write('\n'.join(primes))

i = 1
try:
    while True:
        i += 1
        for d in range(2,round(i/2)+1):
            if i % d == 0: 
                break
        else:
            primes.append(str(i))
            print(i)
except KeyboardInterrupt:
    writeToFile()

atexit.register(writeToFile)