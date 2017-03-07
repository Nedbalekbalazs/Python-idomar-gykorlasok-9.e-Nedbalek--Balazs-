
lottószámok1 = [13, 40, 6, 12, 60, 23]
lottószámok2 = [48, 23, 1, 78, 34, 67]

lottószámok = lottószámok2

for szám in lottószámok:
    if szám > 60 or szám < 40:
        print('Van olyan ami nem 40 és 60 közé esik? ')
        break
else:
    print('Minden szám 40 és 60 közé seik. ')
