

tesztelendő = int(input('Mondjon kend egy számt.'))


if tesztelendő <2:
    print('nem prím')
elif tesztelendő == 2:
    print('prím')
else:
    for szám in range(3, tesztelendő):
        if tesztelendő % szám == 0:
            print('Nem prím. ')
            break
    else:
        print('prím szám')

print('Szeva')    
