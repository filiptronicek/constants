from tqdm import tqdm

d = 1
r = 10000000000

for i in tqdm(range(r)):
    d += d/r
print(d)

with open("outputs/e.txt", "w") as f:
    f.write(str(d))