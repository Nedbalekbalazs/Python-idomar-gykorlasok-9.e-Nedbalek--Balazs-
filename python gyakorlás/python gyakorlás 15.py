kor = 0
while kor/7 + kor/12 + kor/7 + 5 + kor/2 + 4 != kor and kor < 200:
    kor += 1
    print(kor)
if kor < 200:
    print(kor, 'évet élt')    
else:
    print('Nem deríthető ki az életkor.')
