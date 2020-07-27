nums = [0,1]

def calcFi():
    n1 = nums[-2]
    n2 = nums[-1]

    sM = n1 + n2
    phi = sM/n2

    nums.append(sM)

    return (phi)
for i in range(45):
    if i % 15 == 0 or i == 44:
        phi = calcFi()
        print(phi)
        if i == 44: 
            with open("outputs/phi.txt", "w") as f:
                f.write(str(phi))
    else:
        calcFi()