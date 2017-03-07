

hét_napjai = ['hétf', 'kedd', 'szerda', 'csütörtök', 'péntek', 'szombat', 'vasárnap']

napnév = input('Nevezz meg egy napot ').lower()

for nap in hét_napjai:
      if nap == napnév:
          print('Ez egy nap ')
          print('Ügyi vagy tudod a hét napjait mehetsz Hardvardra. Ja nem XD. ')
          break
else:
    print('Hát rossz hírem van ')
    print('Te nagyon hülye vagy sajnálom anyádékat ')
     
