a=str()
b=str()

while not(a.isdigit()) and not(b.isdigit()):
    a=input()
    b=input()
a=int(a)
b=int(b)
print(a+b)