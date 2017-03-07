
számok = [5, 4, 3, 4, 5, 4, 4, 5, 3, 1]


for i in range(1, len(számok)):
    if számok[i] == számok[i-1]:
        print('Van két egymás melletti azonos érték, mégpedig', számok[i], '-ből, a ', i-1, 'és az', i, '.pozíción.', sep='')
        break
else:
    print('Nincs két egymás melletti egyforma érték. ')
        
        
    
