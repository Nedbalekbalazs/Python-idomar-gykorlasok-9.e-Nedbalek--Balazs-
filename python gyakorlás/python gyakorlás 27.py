
zenészek = []
művek = []

számláló = 1

while számláló <=5:
    számláló += 1
    zenész = input('Add meg a' + str(számláló) + 'zenész nevét!')
    mű = input('Add meg a' + str(számláló) + 'mű nevét!')
    zenészek.append(zenész)
    művek.append(mű)
print(zenészek)    
