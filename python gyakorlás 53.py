

gyümölcsök = ['alma', 'körte', 'szilva', 'meggy', 'cseresznye',]

keresett = input('Milyen gyümölcsre vagy kíváncs? ')
for gyömölcs in gyümölcsök:
     if gyümölcs == keresett:
         print('Megvan!  Ő a ', gyümölcsök.index(keresett)+1)
         break
else:
    print('Nincs')

