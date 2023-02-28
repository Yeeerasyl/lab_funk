#+
import random

tup_numbers1=tuple()
tup_numbers2=tuple()
def rand_t_num(n):
    n=tuple(random.randint(0, 5) for i in range(5))
    return n
def rand_t_num_minus(n):
    n=tuple(random.randint(-5, 0) for i in range(5))
    return n

tup_numbers1=rand_t_num(tup_numbers1)
tup_numbers2=rand_t_num_minus(tup_numbers2)
tup_numbers3=tup_numbers1+tup_numbers2
print(tup_numbers3)
print('колличество цифры 0: ',tup_numbers3.count(0))