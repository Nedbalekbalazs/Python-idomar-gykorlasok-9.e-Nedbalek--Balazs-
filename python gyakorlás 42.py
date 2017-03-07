
szám = 0

for szám in range(5 ,501):
    szám += szám
print(szám)



jegyek = []
új_jegy = None
while új_jegy != '':
    új_jegy = input('Adj meg egy jegyet! ') 
    if új_jegy != '':
        új_jegy = int(új_jegy)
    if új_jegy <= 5 and új_jegy >= 1:
        jegyek.append(új_jegy)
        print(jegyek)
    else:
        print('Ilyen jegy nincs ezt meg se hallottam! ')
        

print('Jegyeid:', end='')
for jegy in jegyek:
    print(jegy, ',', sep='', end='')
