#pass
numbers=[]
while True:
    a=int(input())
    
    if a==0:
        break
    numbers.append(a)

numbers.sort()
print(numbers)
