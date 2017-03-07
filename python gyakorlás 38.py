

import random

páros = 0
páratlan = 0

for szám in range(0, 101):
    véletlen = random.randint(1, 6)
    if véletlen % 2 == 1:
        páratlan += 1
    else:
        páros += 1
        
        
if páros > páratlan:
    print('páros volt több', páros, 'darab')
elif páros < páratlan:
    print('páratlan volt több', páratlan, 'darab')
else:
    print('Sosem gondoltam volna, de ilyen is van: \
          egyenlő a párosok és a páratlanok száma.')
