from typing import Callable
somma:Callable[[int], int] = lambda x: x + x
print(somma(6))