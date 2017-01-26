a = int(input('Add meg az "a" oldal hosszát. '))
b = int(input('Add meg a "b" oldal hosszát. '))
c = int(input('Add meg a \'c\' oldal hosszát. '))

if a+c > b and a+b > c and b+c > a:
    print('Ez a háromszög szerkeszthető. ')
else:
    print('Ezekbőlaz oldalakból az életbe\' nem lesz háromszög')
