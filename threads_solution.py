import random, threading, time

array_length = input("Amount of numbers the array should have: ")
number_of_threads = input("Amount of threads for the task: ")

array_length = int(array_length)
number_of_threads = int(number_of_threads)

if number_of_threads > array_length:
    raise Exception(
        "The number of threads cannot be bigger than the length of the array.")

numbers = [random.randint(0, 100) for _ in range(array_length)]
total = 0
threads = list()

def sum_elements(from_index: int, to:int) -> None:
    global total
    result = sum(numbers[from_index:to])
    total += result

incrementor = array_length // number_of_threads
aux = 0
for _ in range(number_of_threads-1):
    # numbers_group = numbers[aux:aux+incrementor]
    thread = threading.Thread(target=sum_elements, args=(aux, aux+incrementor))
    aux += incrementor
    threads.append(thread)

last_thread = threading.Thread(target=sum_elements, args=(aux, array_length))
threads.append(last_thread)

start = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = time.time()

runtime = end - start

print("============results============")
print("total: ", total)
print(f"execution time: {runtime}s")
