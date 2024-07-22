import threading
import random

array_length = input("Amount of numbers the array should have: ")
number_of_threads = input("Amount of threads for the task: ")

array_length = int(array_length)
number_of_threads = int(number_of_threads)

if number_of_threads > array_length:
    raise Exception(
        "The number of threads cannot be bigger than the length of the array.")

numbers = [random.randint(0, 100) for _ in range(array_length)]
threads = list()
total_sum = 0

print("The numbers of the array:")
print(numbers)


def sum_elements(array: list[int]) -> None:
    global total_sum
    result = sum(array)
    total_sum += result


number_of_elements_for_each_group = array_length // number_of_threads
number_of_elements_for_last_group = array_length % number_of_threads

for index in range(number_of_threads-1):
    group_limit_numbers = numbers[index:index +
                                  number_of_elements_for_each_group]

    thread = threading.Thread(target=sum_elements, args=(group_limit_numbers,))
    threads.append(thread)


last_batch_numbers = numbers[len(
    numbers)-number_of_elements_for_last_group-1:]

thread = threading.Thread(target=sum_elements, args=(last_batch_numbers,))
threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("the sum:")
print(total_sum)
