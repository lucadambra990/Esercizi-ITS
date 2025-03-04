def sumNum (a:int, b:int):
    result:int=0
    for i in range(a,b+1):
        result+=i
    return result

somma = sumNum(1,10)
# use sum function to compute a sum of integers from 1 to 10
print(f"La somma dei numeri interi da 1 a 10 è {sumNum(1,10)}")
# use sum function to compute a sum of integers from 20 to 37
print(f"Sum from 20 to 37 is {sumNum(20,37)}")
# use sum function to compute a sum of integers from 35 to 49
print(f"Sum from 35 to 49 is {sumNum(35,49)}")