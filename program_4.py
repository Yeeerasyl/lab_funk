n = int(input()) 
vacations = {} 

for i in range(n):
    name, date = input().split()
    if date in vacations:
        vacations[date].append(name)
    else:
        vacations[date] = [name]

month = input()  
if month in vacations:
    print(*vacations[month]) 