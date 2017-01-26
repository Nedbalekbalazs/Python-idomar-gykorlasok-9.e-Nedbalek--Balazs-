szám1 = input('Mi a szám1? ')
szám2 = input('Mi a szám2? ')
if szám1 > szám2:
    kiírandó = 'Az ' + str(szám1) + ' a nagyobb.'
elif szám1 == szám2:
    kiírandó = 'Egyenlőek.'
else:
    kiírandó = 'A ' + str(szám2) + ' a nagyob.'
print(kiírandó)    
