

gyümölcsök = ['alma', 'körte', 'szilva', 'meggy', 'cseresznye',]

keresett = input('Milyen gyümölcsre vagy kíváncsi. ')

if keresett in gyümölcsök:
    print('Megvan Ő a ', gyümölcsök.index(keresett)+1)
else:
    print('Nincs')
