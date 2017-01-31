név = input('Hogy hívnak ? ')
nem = input('Mi a nemed ? (f/l)  ')
if nem == 'l':
    előtag = 'Ms.'
elif nem == 'f':
    előtag = 'Mr.'
else:
    print('Íly nemet sjna nem ismerek. Nem fogok rendesen köszönni. ')
    előtag = 'M?.'





napszak = input('Milyen napszak van ? (r/du/e/é) ')
if napszak == 'r':
    angol_napszak = 'morning'
elif napszak == 'du':
    angol_napszak = 'afternoon'
elif napszak == 'e':
    angol_napszak = 'evening'
elif napszak == 'é':
    angol_napszak = 'night'
else:
    print('E napszakot sajnos nincs szerencsém ismerni. Aú! Revoár!')
    angol_napszak = 'i-don\'t-know'
print('Good ', angol_napszak, ', ', előtag, ' ', név, '!' , sep='')    

 
