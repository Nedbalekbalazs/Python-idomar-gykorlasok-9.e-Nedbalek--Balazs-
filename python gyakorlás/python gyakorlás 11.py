mettől = int(input('Honnan kezdve írjam ki a számokat?'))
meddig = int(input('Meddig yrjam ki a számokat?'))
hányassával = int(input('Hányassával írjam ki a számokat?'))
hatványkitevő = int(input('Hányadik hatványukat írjam ki a számok mellé?'))

szám = mettől

while szám <= meddig:
    print(szám, szám**hatványkitevő)
    szám = szám + hányassával
