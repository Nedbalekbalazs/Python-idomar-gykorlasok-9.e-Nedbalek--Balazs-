

a = 68
b = 54

for i in range(54, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i, 'A legnagyobb közös osztó')
        break
