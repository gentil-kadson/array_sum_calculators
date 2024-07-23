import threading, time

class ThreadCalculator:
    def __init__(self, numbers: list[int], number_of_threads: int) -> None:
        self.number_of_threads = number_of_threads
        self.array_length = len(numbers)
        self.numbers = numbers
        self.threads = list()
        self.total = 0
        self.time = 0

    def set_time(self, time):
        self.time = time * 1000

    def get_time(self):
        return self.time

    def get_total(self):
        return self.total

    def sum_elements(self, numbers: list[int]) -> None:
        result = sum(numbers)
        self.total += result

    def divide_array_to_threads(self) -> None:
        incrementor = self.array_length // self.number_of_threads
        aux = 0
        for _ in range(self.number_of_threads-1):
            numbers_group = self.numbers[aux:aux+incrementor]
            aux += incrementor
            thread = threading.Thread(target=self.sum_elements, args=(numbers_group,))
            self.threads.append(thread)
        
        last_group_of_numbers = self.numbers[aux:]
        last_thread = threading.Thread(target=self.sum_elements, args=(last_group_of_numbers,))
        self.threads.append(last_thread)

    def calculate_threads_runtime(self) -> None:
        start = time.perf_counter()

        for thread in self.threads:
            thread.start()

        for thread in self.threads:
            thread.join()

        end = time.perf_counter()

        self.set_time(end - start)
