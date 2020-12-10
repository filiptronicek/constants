import atexit
import time, os

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

try:
    while True:
        i += 1
        for d in range(2,round(i/2)+1):
            if i % d == 0: 
                break
        else:
            primes.append(str(i))
            print(i)
            time.sleep(0.01)
except KeyboardInterrupt:
    writeToFile()

atexit.register(writeToFile)