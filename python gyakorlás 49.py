

vezérek = ['Áloms', 'Előd', 'Ond', 'Kond', 'Tas', 'Huba', 'Töhötöm']

kit = input('Kit keresünk? ')


for i in range(len(vezérek)):
    if  vezérek[i] == kit:
        van_Ond = True
        print('A', kit, 'vezér a ', i+1, 'a sorban', sep='')
        break
else:
    print('Nem volt ', kit)
        

