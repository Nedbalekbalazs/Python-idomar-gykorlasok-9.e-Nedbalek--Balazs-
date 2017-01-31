ALSÓ_HATÁR = int(input('Melyik legyen a legalacsonyabb szám?'))
FELSŐ_HATÁR = int(input('Melyik legyen a legmagasabb szám?'))



sikeres = 0
sikertelen = 0
import random

gondolt_szám = random.randint(1, 5)

kitalálta = False
elhasznált_lehetőségek = 0

while not kitalálta and elhasznált_lehetőségek < 3:
    tipp = input('Melyik számra gondoltam' + str(ALSÓ_HATÁR) + 'és' + str(FELSŐ_HATÁR) + 'között' )
    tipp = int(tipp)
    elhasznált_lehetőségek += 1
    if tipp == gondolt_szám:
        kitalálta = True
        print('Ügyes!') 
if not kitalálta:
    print('Te vad barom! ')
if kitalálta or not kitalálta: 
    print('Játszunk mégegyet?' )
         
print('Pápá!')        
    

