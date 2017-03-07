import random

szám = 999
kísérlet = 0

while szám % 2 != 0:
    kísérlet += 1
    szám = random.randint(1, 100)
    print('A', kísérlet, '.dobás eredménye:', szám, '.', sep='' )

print('A', kísérlet, '.dobás járt eredménnyel:', szám, '.', sep='' )    
