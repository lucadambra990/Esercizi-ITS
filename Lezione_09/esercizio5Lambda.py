from typing import Callable
pari_dispari:Callable[[int],str] = lambda x: "Pari" if x%2==0 else "Dispari"
print(pari_dispari(5))
print(pari_dispari(2))