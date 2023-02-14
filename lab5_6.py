#pass
def check_sort(numbers):
    if numbers==sorted(numbers):
        print("True")
    else:
        print("False")


numbers=[]
for i in range(5):
    i=int(input())
    numbers.append(i)

check_sort(numbers)
