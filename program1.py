# tuple
numbers=[1,23,5,4345,4,2,5,6,6,23]
tuple_numbers=tuple(numbers)
print(tuple_numbers)
print(tuple_numbers[2:5:2])
print('len: ',len(tuple_numbers))
print(tuple_numbers.index(23))
print(tuple_numbers.count(23))
print(tuple_numbers*3)
print()
print()
# set
set_numbers=set(numbers)
print(set_numbers)
print(len(set_numbers))
print(2 in set_numbers)
set_numbers.add(3)
set_numbers.remove(2)
print(set_numbers)
print(set_numbers.clear())
print('set: ',set_numbers)