import math
def safe_sqrt(number:int):
    try: 
        print(math.sqrt(number))
    except ValueError as error:
        print(error)

safe_sqrt(-9)
