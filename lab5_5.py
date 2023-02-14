#pass
import random
win=[1,10,22,39,40]
numbers = random.sample(range(1, 49), 5)

numbers.sort()
print(numbers)
if (win==numbers):
    print("You win")
else:
    print("You lose")