gyümölcsök = ['alma', 'körte', 'szilva', 'meggy', 'cseresznye',]

keresett = input('Milyen gyümölcsre vagy kíváncsi. ')


for i in range(len(gyümölcsök)):
     if gyümölcsök[i] == keresett:
         print('Megvan!  Ő a ', i+1)
         break
else:
    print('Nincs')
