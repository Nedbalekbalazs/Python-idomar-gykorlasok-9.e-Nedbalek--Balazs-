if True:
    print('igaz')

if False:
    print('hamis')

if not True:
    print('Nem igaz-azaz hamis ')

if not False:
    print('Nem hamis-azaz igaz')

doboz = None
if doboz:
    print('1-Most van benne valami')
if not doboz:
    print('1-Most üres')


doboz = ''
if doboz:
    print('2-Most van benne valami')
if not doboz:
    print('"-Most üres ')

doboz = 'ezt tettem bele'
if doboz:
    print('3-Most van benne valami ')
if doboz:
    print('3-Most üres')
