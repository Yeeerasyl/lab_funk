word=str(input('введите слово: '))
count_UP=0
count_LOW=0

for i in word:
    if i.islower():
        count_LOW+=1
    if i.isupper():
        count_UP+=1

if (count_UP>count_LOW):
    print('Больших букв больше чем маленьких букв. Кол-во: ', count_LOW)
    print(word.upper())
else:
    print('Маленьких букв больше чем больших букв. Кол-во: ', count_LOW)
    print(word.lower())