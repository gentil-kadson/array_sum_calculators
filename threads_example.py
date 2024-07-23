from thread_calculator import ThreadCalculator
import random

array_length = input("Amount of numbers the array should have: ")
number_of_threads = input("Amount of threads for the task: ")

array_length = int(array_length)
number_of_threads = int(number_of_threads)

if number_of_threads > array_length:
    raise Exception(
        "The number of threads cannot be bigger than the length of the array.")

numbers = [random.randint(0, 100) for _ in range(array_length)]

calculator = ThreadCalculator(numbers, number_of_threads)
calculator.divide_array_to_threads()
calculator.calculate_threads_runtime()

print("============results============")
print("total: ", calculator.get_total())
print(f"execution time: {calculator.get_time()}ms")
