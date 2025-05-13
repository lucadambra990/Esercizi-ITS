def primo(n:int)->bool:
    for i in range(n-1, 1, -1):
        if n%i==0:
            return False
        
    return True
print(primo(7))





# lista interi disordinata, restituire un'altra lista di interi ordinata dal più piccolo al più grande, se il primo è più piccolo del secondo, sono ordinati
# se non è così devo scambiarli, fallo per casa!!! Bisogna usare due cicli, uno scorre uno fa lo swap, la lista deve scorrere n volte e fare lo swap.
# creare un algoritmo siml bubbleSort