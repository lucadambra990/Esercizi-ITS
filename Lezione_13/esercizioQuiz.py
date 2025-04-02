def recursicePower(base:int,exponent:int):
    if exponent==0:
        return 1
    else:
        return int(base * recursicePower(base, exponent - 1))
    
print(recursicePower(3,4))