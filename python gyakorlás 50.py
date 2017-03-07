
számok = [1, 54, 35, 67, 12]

for szám in számok:
    if szám % 2 == 0:
        print('Az első páros a', szám)
        break

for szám in számok:
    if szám % 7 == 0:
        print('Az első héttel osztható a', szám)
        break

for szám in számok:
    if 60 < 70:
        print('Az első 60-70 között a', szám)
        break


for i in range(len(számok)):
    if számok[i] == 12:
        print('A 12 a ', i+1, 'a sorban az indexe: ', i, '.', sep='')
        break
    

    



    
