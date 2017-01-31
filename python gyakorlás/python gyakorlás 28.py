
írók = []
művek = []

író = None

while író != '':
    író = input('Add meg az író nevét')
    if író:
        írók.append(író)

for író in írók:
    mű = input('add meg' + író + 'egy művét' )
    művek.append(mű)
print(írók, '\n', művek)
