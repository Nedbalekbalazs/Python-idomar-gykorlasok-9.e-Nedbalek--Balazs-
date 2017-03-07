
#sorozat számitás

számlista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

összeg = 0
for szám in számlista:
    összeg += szám

print(összeg)
print(sum(számlista))


összeg = 0
elemszám = 0
for szám in számlista:
    összeg += szám
    elemszám += 1

print(összeg/elemszám)
print(sum(számlista))

szorzat = 1
for szám in  számlista:
    szorzat *= szám
    print(szorzat)


betűk = ['E', 'n', 'n', 'y', 'i']

szöveg = ''

for betű in betűk:
    szöveg += betű
    print(szöveg) 
