
import random

dado = random.randint(1, 6)
print(f"El dado sacó: {dado}")

if dado % 2 == 0:
    print("hola")
else:
    print("adiós")