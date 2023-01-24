import random
a=int(input("угадайте рандомную цифру: "))
b=(random.randint(0,10))

if (a==b):
    print("поздравляю вы угадали рандомную цифру")
else:
    print("вы не угадали рандомную цифру")

print("рандомная цифра была: ",b)