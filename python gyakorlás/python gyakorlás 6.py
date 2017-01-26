gondolt_szám = 3
tipp = input('Szerinted melyik számra gondolok 1 és 5 között?')
tipp = int(tipp)
if gondolt_szám == tipp:
    print('Eltaláltad.')
    print('Kis ügyes.')
elif abs(tipp - gondolt_szám) == 1:
    print('Majdnem!....')
else:
    print('Ez most sajnos nem sikerült... ')
print('Pápá!')    
