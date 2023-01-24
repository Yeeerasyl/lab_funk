import math
a=int(input("a= "))
j=0
#квадраты
print("квадраты")
while (a>j):
    j=j+1
    print(pow(j,2))
#корни
print("корни")
for i in range(a):
    print(math.sqrt(i))