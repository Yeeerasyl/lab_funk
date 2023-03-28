n = int(input())
rivers = {}
for i in range(n):
    country, names = input().split()
    for name in names:
        rivers[name] = country

for name in input().split():
    if name in rivers:
        print(f'{name} - {rivers[name]}')
    else:
        print(f'{name} - не найдена')
''' 4
Kazakhstan Ertis
USA Mississippi
Brazil Amazonka
Canada Mazzenki
 '''