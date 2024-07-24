import random, time

array_length = input("Amount of numbers the array should have: ")
array_length = int(array_length)
numbers = [random.randint(0, 100) for _ in range(array_length)]

start = time.time()

total = sum(numbers)

end = time.time()
execution_time = end - start

print("============results============")
print("total:", total)
print(f"execution time: {execution_time}s")
