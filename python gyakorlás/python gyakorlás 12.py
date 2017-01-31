#if (pulyka or marha or sonka)
#(marha and not sonka) or (sonka nad not marha)
#(pulyka and sajt) or (not pulyka)
pulyka = False
marha = False
sonka = False
sajt = False

válasz = input('Van benne pulyka? (i/n)')
if válasz == 'i':
    pulyka = True


válasz = input('Van benne marha? (i/n)')
if válasz == 'i':
    marha = True


válasz = input('Van benne sonka? (i/n)')
if válasz == 'i':
    sonka = True


válasz = input('Van benne sajt? (i/n)')
if válasz == 'i':
    sajt = True

if (pulyka or marha or sonka) and \
   ((marha and not sonka) or (sonka and not marha)) and \
   ((pulyka and sajt) or (not pulyka)):
   print('Nyamnyam')
else:
    print('Hulladék')
