def prime_factors(n: int) -> list[int]:
    n_factor:list[int] = []
    div=2
    while n>1:
        while n%div==0:
            n_factor.append(div)
            n//=div
        div+=1
    return n_factor


            

print(prime_factors(4))