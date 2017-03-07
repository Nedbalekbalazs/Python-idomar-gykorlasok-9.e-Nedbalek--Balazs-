


számok = [1, 5, 67, 23, 433, 64, 43, 32, 49, 54, 545]

van64 = False

i = 0
while i < len(számok)and not van64:
    if számok[i] == 64:
        van64 = True 
    i += 1


if van64:
    print('Van ám')
else:
    print('Nem van')

for szám in számok:
    print(szám)
    if szám == 64:
        print('Van ám')
        break
