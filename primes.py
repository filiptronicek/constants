import atexit
import os

primes = []

def writeToFile():
    with open("outputs/primes.txt", "w") as f:
        f.write('\n'.join(primes))

def loadCheckPoint():
    if os.path.exists('outputs/primes.txt'):
        with open('outputs/primes.txt') as f:
            for line in f:
                pass
            return int(line)
    else:
        return 1

i = loadCheckPoint()

def isPrime(n) : 
 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
 
    # This is checked so that we can skip 
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True

try:
    while True:
        i += 1
        if isPrime(i):
            primes.append(str(i))
            print(i)
        else:
            if i % 1000000 == 0:
                writeToFile()    
        
except KeyboardInterrupt:
    writeToFile()

atexit.register(writeToFile)