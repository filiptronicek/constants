import math

def e(n=10):
    return sum(1 / float(math.factorial(i)) for i in range(n))
print(e(40))

with open("outputs/e.txt", "w") as f:
    f.write(str(e(40)))

# Parts of code taken from https://stackoverflow.com/a/23442735/10199319