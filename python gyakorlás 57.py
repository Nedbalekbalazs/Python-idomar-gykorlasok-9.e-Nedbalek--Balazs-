


betűk = ['a', 'v', 'b', 'k', 'a', 'f', 'i', 'm', 'o', 'a',]

k_utániak = 0
a_k_száma = 0

for betű in betűk:
    if betű > 'k':
        print(betű)
        k_utániak += 1
    if betű == 'a':
        a_k_száma += 1

print(k_utániak, 'darab betű volt a \'k\' után.')
print(a_k_száma, '"a" betű volt')
        
