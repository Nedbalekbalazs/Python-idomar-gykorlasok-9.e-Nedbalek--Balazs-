gondolt_szám = 4

 
kitalálta = False

elhasznált_lehetőségek = 0

while not kitalálta and elhasznált_lehetőségek < 3:
    tipp = int(input('Melyik számra gondoltam 1 és 5 között?'))
    elhasznált_lehetőségek += 1
    if tipp == gondolt_szám:
         kitalált = True
    elif tipp > gondolt_szám:
        print('Tippelj kisebbet.')
    else:
        print('Tippel nagyobbat.')
    
print('Csá!')                 
