

import random

véletlenszámok = []

hatosok = 0

for _ in range(100000):
    véletlenszámok = random.randint(1, 6)
    véletlenszámok.append(véletlenszám)
    if véletlenszámok == 6:
        hatosok +=1

print(hatosok, 'hatos van')    
