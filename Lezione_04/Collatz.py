import matplotlib.pyplot as plt
def collatz(n:float)-> list[float]:
    numeri:list=[n]

    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n = (3*n) + 1
        
        numeri.append(n)
    return numeri

print(collatz(8))


numeri:list[float] = collatz(9.0)
plt.plot(numeri)
plt.show()