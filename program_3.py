n = int(input())
phonebook = {} 

for i in range(n):
    phone, name = input().split()
    phonebook[phone] = name

nameee = input()
if nameee in phonebook:
    print(phonebook[nameee])
else:
    print("Нет в телефонной книге")

