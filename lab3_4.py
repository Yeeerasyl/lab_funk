n=int(input("n= "))
sum1=0
sum2=0
for i in range (1,n+1):
    sum1+=i

for i in range (1,n):
    sum2+=int(input("введите цифру которую знаете: "))

print ("потеренная цифра=", sum1-sum2)